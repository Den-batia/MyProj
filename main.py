import Cena
import time
import random
import threading
import re
import datetime
import time

time_sleep = 0

proxy = ['193.111.152.224:4734', '193.111.152.95:4734', '193.111.152.122:4734',
         '193.111.152.98:4734', '193.111.152.239:4734', '93.111.152.106:4734',
         '193.111.152.248:4734', '193.111.152.119:4734', '193.111.152.80:4734',
         '193.111.152.185:4734', '193.111.152.36:4734', '193.111.152.238:4734',
         '193.111.152.85:4734', '193.111.152.57:4734', '193.111.152.116:4734',
         '193.111.152.14:4734', '193.111.152.28:4734', '193.111.152.207:4734',
         '193.111.152.32:4734', '193.111.152.164:4734', '193.111.152.117:4734',
         '193.111.152.209:4734', '193.111.152.129:4734', '193.111.152.251:4734',
         '193.111.152.8:4734', '193.111.152.89:4734', '193.111.152.186:4734',
         '193.111.152.38:4734', '193.111.152.128:4734']


class Tm:

    def __init__(self):
        self.lock = threading.Lock()
        self.r = []

    def a(self, time, r):
        global time_sleep
        with self.lock:
            if self.r is not None:
                self.r.clear()

            list_price = re.findall(r'<td class="column-price"\s*\W*.*', r)
            for x in list_price:
                t = re.search(r'\d{2}\D\d{3}\D\d{2}', x)
                t = t.span()
                self.r.append(x[t[0]:t[1]])
            self.r.sort()
            # t = re.search(r'\d{2}\D\d{3}\D\d{2}', self.r[0])
            # print(self.r[0][63:72])
            # print(self.r)
            time_sleep = (time_sleep + time) / 2

    def rr(self):
        with self.lock:
            return self.r


if __name__ == '__main__':
    tm = Tm()

    Cena.Torg(tm)
    while True:
        for pr in proxy:
            a = Cena.Cena(pr, tm)
            a.start()
            time.sleep(time_sleep)
            print(time_sleep)
