from datetime import *
import requests
import time
import conf

def start(proxy, tm):

    t_1 = datetime.now()
    s = requests.Session()
    s.proxies = {'https': conf.proxy_logpas + proxy}
    r = s.get(conf.url).text
    s.close()
    t_2 = datetime.now()
    time = t_2 - t_1
    tm.a(time.microseconds / 1000000, r)

def start1(tm):

    while True:
        r = dict.copy(tm.rr())
        if r is None:
            continue
        else:
            print(r, end='\n')
        time.sleep(0.3)
