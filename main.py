from concurrent import futures
import time
import threads_methods
import conf
import Html_requests
import multiprocessing
import queue



'''
    Старт скрипта
'''

if __name__ == '__main__':
    q = multiprocessing.Queue()
    multiprocessing.Process(target=threads_methods.start1, args=(q,)).start()
    while True:
        for pr in conf.proxy:
            multiprocessing.Process(target=threads_methods.start, args=(pr, q,)).start()
            time.sleep(0.2)

