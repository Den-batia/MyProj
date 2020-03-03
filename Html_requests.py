import threading
import re
import conf
'''
    Синхро женерик клаcс, получает реквесты с фабри потоков(синхронно),
    парсит, получает словарь ник:текущая цена. Словарь не отсортирован.
    Также синхронно возвращает словать в отдельный поток изменения цены.
'''

class Tm:

    def __init__(self):
        self.lock = threading.Lock()
        self.r = {}

    def a(self, r):
        global time_sleep

        with self.lock:
            if self.r is not None:
                self.r.clear()
            # список текущих цен
            list_price = re.findall(r'<td class="column-price">\s*\W*(\d{2}\D\d{3}\D\d{2})', r)
            # список текущих имен
            list_names = re.findall(r'<a href="/accounts/profile/(\w*)', r)
            # словарь имя:цена
            self.r = {list_names[name]: str(list_price[name]).replace(',', '') for name in range(len(list_price))}
            list_price.clear()
            list_names.clear()



    def rr(self):
        with self.lock:
            return self.r
