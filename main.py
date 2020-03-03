from concurrent import futures
import time
import threads_methods
import conf
import Html_requests
'''
    Старт скрипта
'''

if __name__ == '__main__':

    tm = Html_requests.Tm()
    with  futures.ThreadPoolExecutor(max_workers=15) as pool:

        # поток изменения моей цены
        pool.submit(threads_methods.start1, tm)

        # поток отправки первого сообщения
        # pool.submit(threads_methods.first_mess)

        # генератор потоков для полученя реквестов
        while True:
            for pr in conf.proxy:
                pool.submit(threads_methods.start, pr, tm)
                time.sleep(0.4)



