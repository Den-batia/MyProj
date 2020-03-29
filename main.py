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
    tm = Html_requests.Tm()
    # threading.Thread(target=threads_methods.start1, args=(tm,)).start()
    q = multiprocessing.Queue()
    multiprocessing.Process(target=threads_methods.q, args=(q,)).start()
    # with futures.ProcessPoolExecutor(max_workers=2) as pool:
    #
    #     pool.submit(threads_methods.q, qq)
    a = 0
    while True:
        q.put(a)
        a+=1
        time.sleep(0.5)
        # for pr in conf.proxy1:
        #     Process(target=threads_methods.start, args=(pr, q,)).start()
        #     time.sleep(0.6)
    # with  futures.ProcessPoolExecutor(max_workers=4) as pool:
    #
    # #
    # #     # поток изменения моей цены
    # #     # pool.submit(threads_methods.start1, tm)
    # #
    # #     # поток отправки первого сообщения
    # #     # pool.submit(threads_methods.first_mess)
    # #
    # #     # генератор потоков для полученя реквестов
    #     while True:
    #         for pr in conf.proxy1:
    #             pool.submit(threads_methods.start, pr, q)
    #             time.sleep(0.5)
