from threading import Thread
import time
from random import randint


class My_Thread(Thread):
    def __init__(self, name):
        super(My_Thread, self).__init__()
        self.name = name

    def run(self):
        a = randint(0, 10)
        time.sleep(a)
        print(self.__str__() + ' конец ' + str(a) + ' sec\n')

    def __str__(self):
        return 'Tread № ' + str(self.name)


def method(nam):
    a = randint(0, 10)
    time.sleep(a)
    print(nam + ' конец ' + str(a) + ' sec\n')


for a in range(0, 30):
    ss = Thread(target=method, args=(str(a)))
    ss.start()