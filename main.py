import Cena
import time
import random
import threading
import concurrent.futures
import requests

sell_list = "https://localbitcoins.net/ru/buy-bitcoins-online/byn/"
url = sell_list + '.json'
time_sleep = 0
d = {1, 2, 3}
proxy = ['134.0.116.135:3128', '193.124.46.245:3128', '193.124.46.39:3128',
         '193.124.46.64:3128', '193.124.46.248:3128', '193.124.46.235:3128',
         '193.124.46.236:3128', '193.124.46.149:3128', '193.124.46.176:3128',
         '193.124.46.85:3128']

proxy_logpas = '//user39773:rdwa08@'


class Tm:

    def __init__(self):
        self.lock = threading.Lock()
        self.r = None

    def a(self, time, r):
        global time_sleep
        with self.lock:
            self.r = r
            print(self.r)
            # time_sleep = (time_sleep + time) / 2


    def rr(self):
        with self.lock:
            return self.r


if __name__ == '__main__':
    tm = Tm()
    s = requests.Session()
    Cena.Torg(tm)
    while True:
        for pr in range(9):
            a = Cena.Cena(proxy[pr], tm)
            a.start()

            time.sleep(0.3)
        print(threading.active_count())

    # a.join()
    # print(a.is_alive())
    # print(a)
    # print(price)
    # print(r)r
