import threading

from datetime import *
import requests
import json
import time
import math
import random

sell_list = "https://localbitcoins.net/ru/buy-bitcoins-online/byn/"
url = sell_list + '.json'
proxy_logpas = '//user39773:rdwa08@'


class Cena(threading.Thread):
    def __init__(self, proxy, tm):
        super(Cena, self).__init__()
        self.proxy = proxy
        self.tm = tm

    def run(self) -> None:
        t_1 = datetime.now()
        s = requests.Session()
        # print(self.proxy + str(self.tm))
        s.proxies = {'http': proxy_logpas + self.proxy}
        r = s.get(url).json()
        t_2 = datetime.now()
        self.tm.a((t_2 - t_1).microseconds / 1000000, r)
        #print(self.proxy + threading.currentThread().name)


class Torg(threading.Thread):
    def __init__(self, tm):
        super(Torg, self).__init__()
        self.tm = tm

    def run(self) -> None:

        while True:
            r = self.tm.rr()
            if r is None:
                continue
            else:
                print(r.text)
            time.sleep(0.3)


