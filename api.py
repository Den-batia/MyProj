import datetime
import hashlib
import hmac as hmac_lib
import requests
import time
import urllib.parse



def oauth2(
    access_token,
    client_id,
    client_secret=None,
    refresh_token=None,
    expires_at=None,
    server="https://localbitcoins.com",):
    conn = Connection()
    conn._set_oauth2(
        server, client_id, client_secret, access_token, refresh_token, expires_at
    )
    return conn


def hmac(hmac_key, hmac_secret, server="https://localbitcoins.com", proxy=None):
    conn = Connection()
    conn._set_hmac(server, hmac_key, hmac_secret, proxy)
    return conn


class Connection:
    def __init__(self):
        self.server = None

        # OAuth2 stuff
        self.client_id = None
        self.client_secret = None
        self.access_token = None
        self.refresh_token = None
        self.expires_at = None
        self.proxy = None

        # HMAC stuff
        self.hmac_key = None
        self.hmac_secret = None
    def proxxy(self):
        print(self.proxy)
    def call(self, method, url, params=None, stream=False, files=None):
        method = method.upper()
        if method not in ["GET", "POST"]:
            raise Exception("Invalid method {}!".format(method))

        if method == "GET" and files:
            raise Exception("You cannot send files with GET method!")

        # If URL is absolute, then convert it
        if url.startswith(self.server):
            url = url[len(self.server) :]

        # If OAuth2
        if self.access_token:

            # If token is expiring tomorrow, then try to refresh it
            if (
                self.refresh_token
                and self.client_id
                and self.client_secret
                and (
                    not self.expires_at
                    or self.expires_at
                    < datetime.datetime.utcnow() + datetime.timedelta(days=1)
                )
            ):
                refresh_params = {
                    "refresh_token": self.refresh_token,
                    "grant_type": "refresh_token",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                }
                r = requests.post(
                    self.server + "/oauth2/access_token/", data=refresh_params
                )
                self.access_token = r.json()["access_token"]
                self.refresh_token = r.json()["refresh_token"]
                self.expires_at = datetime.datetime.utcnow() + datetime.timedelta(
                    seconds=int(r.json()["expires_in"])
                )

            headers = {"Authorization-Extra": "Bearer " + self.access_token}

            if method == "GET":
                return requests.get(self.server + url, params=params, headers=headers)
            else:
                return requests.post(
                    self.server + url,
                    data=params,
                    headers=headers,
                    stream=stream,
                    files=files,
                )

        # If HMAC
        elif self.hmac_key:
            # If nonce fails, retry several times, then give up
            for retry in range(10):

                nonce = str(int(time.time() * 1000))
                # Prepare request based on method.
                if method == "POST":
                    api_request = requests.Request(
                        "POST", self.server + url, data=params, files=files
                    ).prepare()
                    params_encoded = api_request.body


                # GET method
                else:
                    api_request = requests.Request(
                        "GET", self.server + url, params=params
                    ).prepare()
                    params_encoded = urllib.parse.urlparse(api_request.url).query

                # Calculate signature
                message = nonce + self.hmac_key + str(url)
                if params_encoded:
                    message += str(params_encoded)
                hmac_secret_bytes = bytes(self.hmac_secret, "utf-8")
                message_bytes = bytes(message, "utf-8")
                signature = (
                    hmac_lib.new(
                        hmac_secret_bytes, msg=message_bytes, digestmod=hashlib.sha256
                    )
                    .hexdigest()
                    .upper()
                )

                # Store signature and other stuff to headers
                api_request.headers["Apiauth-Key"] = self.hmac_key
                api_request.headers["Apiauth-Nonce"] = nonce
                api_request.headers["Apiauth-Signature"] = signature

                # Send request
                session = requests.Session()
                session.proxies = self.proxy
                response = session.send(api_request, stream=stream)

                # If HMAC Nonce is already used, then wait a little and try again
                try:
                    response_json = response.json()
                    if int(response_json.get("error", {}).get("error_code")) == 42:
                        time.sleep(0.1)
                        continue
                except:
                    # No JSONic response, or interrupt, better just give up
                    pass

                return response

            raise Exception("Nonce is too small!")
        raise Exception("No OAuth2 or HMAC connection initialized!")

    def get_access_token(self):
        return self.access_token

    def get_refresh_token(self):
        return self.refresh_token

    def get_expires_at(self):
        return self.expires_at

    def _set_oauth2(
        self, server, client_id, client_secret, access_token, refresh_token, expires_at
    ):
        self.server = server
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at
        self.hmac_key = None
        self.hmac_secret = None

    def _set_hmac(self, server, hmac_key, hmac_secret, proxy):
        self.server = server
        self.client_id = None
        self.client_secret = None
        self.access_token = None
        self.refresh_token = None
        self.expires_at = None
        self.proxy = proxy
        self.hmac_key = str(hmac_key)
        self.hmac_secret = str(hmac_secret)
