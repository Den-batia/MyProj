import threading
import re
import conf


class Tm:

    def __init__(self):
        self.lock = threading.Lock()
        self.r = {}

    def a(self, time, r):
        global time_sleep

        with self.lock:
            if self.r is not None:
                self.r.clear()
            list_price = re.findall(r'<td class="column-price">\s*\W*(\d{2}\D\d{3}\D\d{2})', r)
            list_names = re.findall(r'<a href="/accounts/profile/(\w*)', r)
            self.r = {list_names[name]: str(list_price[name]).replace(',', '') for name in range(len(list_price))}
            list_price.clear()
            list_names.clear()

            conf.av_times_list.append(time)


    def rr(self):
        with self.lock:
            return self.r
