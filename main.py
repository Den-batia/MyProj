import Cena
import time
import random
import threading

time_sleep = 0
proxy = ['193.111.152.224:4734', '193.111.152.95:4734', '193.111.152.122:4734',
         '193.111.152.98:4734', '193.111.152.239:4734', '93.111.152.106:4734',
         '193.111.152.248:4734', '193.111.152.119:4734', '193.111.152.80:4734',
         '193.111.152.185:4734', '193.111.152.36:4734', '193.111.152.238:4734',
         '193.111.152.85:4734', '193.111.152.57:4734', '193.111.152.116:4734',
         '193.111.152.14:4734', '193.111.152.28:4734', '193.111.152.207:4734',
         '193.111.152.32:4734', '193.111.152.164:4734', '193.111.152.117:4734']
# 193.111.152.209:4734:user39773:rdwa08
# 193.111.152.129:4734:user39773:rdwa08
# 193.111.152.251:4734:user39773:rdwa08
# 193.111.152.8:4734:user39773:rdwa08
# 193.111.152.89:4734:user39773:rdwa08
# 193.111.152.186:4734:user39773:rdwa08
# 193.111.152.38:4734:user39773:rdwa08
# 193.111.152.128:4734:user39773:rdwa08]

class Tm:

    def __init__(self):
        self.lock = threading.Lock()
        self.r = None

    def a(self, time, r):
        global time_sleep
        with self.lock:
            self.r = r
            print(self.r)
            time_sleep = (time_sleep + time) / 2

    def rr(self):
        with self.lock:
            return self.r


if __name__ == '__main__':
    tm = Tm()

    Cena.Torg(tm)
    while True:
        print(len(proxy))
        for pr in proxy:
            a = Cena.Cena(pr, tm)
            a.start()
            time.sleep(time_sleep+0.2)
        print(threading.active_count())


