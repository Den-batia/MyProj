import threading
'''
    Синхро женерик клаcс, получает словарь с фабри потоков(синхронно).
    Также синхронно возвращает словать в отдельный поток изменения цены.
'''

class Tm:

    def __init__(self):
        self.lock = threading.Lock()
        self.r = {}

    def a(self, r):
        with self.lock:
            if self.r is not None:
                self.r.clear()
            self.r = r
            


    def rr(self):
        with self.lock:
            return self.r
