from concurrent import futures
import time
import threads_methods
import conf
import Html_requests


if __name__ == '__main__':
    tm = Html_requests.Tm()
    with  futures.ThreadPoolExecutor(max_workers=15) as pool:
        pool.submit(threads_methods.start1, tm)
        # pool.submit(threads_methods.first_mess)

        while True:
            for pr in conf.proxy:
                pool.submit(threads_methods.start, pr, tm)
                time.sleep(0.4)



