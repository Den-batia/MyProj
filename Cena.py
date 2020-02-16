import threading

from datetime import *
import requests
from Main import *
sell_list= "https://localbitcoins.net/ru/buy-bitcoins-online/byn/"
url = sell_list + '.json'
proxy_logpas = '//user39773:rdwa08@'


class Cena(threading.Thread):

    def __init__(self, proxy, time):
        super(Cena, self).__init__()
        self.proxy = proxy
        self.time = time

    def run(self) -> None:
        t_1 = datetime.now()
        s = requests.Session()
        s.proxies = {'http': proxy_logpas + self.proxy}
        r = s.get(url).json()['data']['ad_list']
        t_2 = datetime.now()
        print(t_2 - t_1)