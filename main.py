import threads_methods
import conf
import threading
import re
from concurrent import futures
import time


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
                self.r.append(float(x[t[0]:t[1]].replace(',', '')))
            self.r.sort()
            # t = re.search(r'\d{2}\D\d{3}\D\d{2}', self.r[0])
            conf.time_sleep = (conf.time_sleep + time) / 2

    def rr(self):
        with self.lock:
            return self.r


if __name__ == '__main__':
    tm = Tm()
    with  futures.ThreadPoolExecutor(max_workers=6) as pool:
        pool.submit(threads_methods.start1, tm)
        while True:
            for pr in conf.proxy:
                pool.submit(threads_methods.start, pr, tm)
                time.sleep(conf.time_sleep/3)

