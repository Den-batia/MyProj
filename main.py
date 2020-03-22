from concurrent import futures
import time
import threads_methods
import conf
import Html_requests
import threading
'''
    Старт скрипта
'''

if __name__ == '__main__':
    tm = Html_requests.Tm()
    # threading.Thread(target=threads_methods.start1, args=(tm,)).start()

    with  futures.ThreadPoolExecutor(max_workers=30) as pool:

        pool.submit(threads_methods.bay)
        # поток изменения моей цены
        # pool.submit(threads_methods.start1, tm)

        # поток отправки первого сообщения
        # pool.submit(threads_methods.first_mess)

        # генератор потоков для полученя реквестов

        # while True:
        #     for pr in conf.proxy1:
        #         pool.submit(threads_methods.start, pr, tm)
        #         time.sleep(0.1)



