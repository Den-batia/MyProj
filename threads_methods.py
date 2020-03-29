from datetime import *
import requests
import time
import datetime
import re
import threading
import conf
import api
import API_keys

'''
    Методы для фабрики потоков 
'''
def q(q):

    while True:
        try:
            a = q.get()
            while not q.empty():
                a = q.get()
            print(a)
            print(q.qsize())
            time.sleep(1)
        except Exception as e:
            print(e)
def start(proxy, q):
    t0 = datetime.datetime.now()
    # поток получения реквеста через прокси
    s = requests.Session()
    s.proxies = {'https': conf.proxy1_logpas + proxy}
    r = s.get(conf.url).text
    s.close()
    del s
    # список текущих цен
    list_price = re.findall(r'<td class="column-price">\s*\W*(\d{2}\D\d{3}\D\d{2})', r)
    # список текущих имен
    list_names = re.findall(r'<a href="/accounts/profile/(\w*)', r)
    # словарь имя:цена
    r = {list_names[name]: str(list_price[name]).replace(',', '') for name in range(len(list_price))}
    # print(datetime.datetime.now()- t0)
    q.put(r)

def start1(tm):
    # поток измения моей цены

    while True:
        for proxy in range(len(conf.proxy)):
            pr = conf.proxy[proxy]
            r = dict.copy(tm.rr())
            list_l = []
            if r is None:
                continue
            else:
                for trader in r.keys():
                    if trader in conf.list_ignore or float(r[trader]) < conf.Low:
                        continue
                    else:
                        list_l.append(r[trader])
                if len(list_l) > 0:
                    print(pr, end=' ')
                    min_price = float(list_l[0])
                    my_new_price = str(round(min_price - conf.X, 2))
                    params = {u'price_equation': my_new_price}
                    try:
                        conn = api.hmac(API_keys.hmac_key, API_keys.hmac_secret, proxy={'https': conf.proxy_logpas + pr})
                        a = conn.call('POST', conf.Me_3, params).json()
                        print(a, my_new_price)
                        del conn
                    except Exception as e:
                        print(e)



def first_mess():
    # поток отправки первого сообщения
    conn = api.hmac(API_keys.hmac_key, API_keys.hmac_secret)
    n = None
    while True:
        try:
            n = conn.call('GET', '/api/notifications/').json()['data']
        except Exception as e:
            print(e)

        for i, e in reversed(list(enumerate(n))):

            if e['read'] == False:
                s = e['msg']  # тело сообщения
                d = str(e['id'])  # id сообщения
                d1 = str('/api/notifications/mark_as_read/' + d + '/')  # api ключ
                k = str(e['contact_id'])  # id сделки
                k1 = str('/api/contact_message_post/' + k + '/')

                if 'Вы получили новое предложение' in s:
                    print('есть сообщение!')
                    '''
                    print('начинаем процесс отправки реквезитов!!!')
                    conn.call('POST', k1, conf.MyMess).json()
                    conn.call('POST', d1).json()
                    print('\t реквезиты отправлены.\n')
                    # logging.info('Реквизиты отправлены. ID сделки: ' + k)
                    continue
                    '''
        time.sleep(4)
        print('идем далше')

def bay():
    while True:
        list_l = []
        s = requests.Session()
        r = s.get(conf.url_2).text
        s.close()
        del s
        list_price = re.findall(r'<td class="column-price">\s*\W*(\d{2}\D\d{3}\D\d{2})', r)
        list_names = re.findall(r'<a href="/accounts/profile/(\w*)', r)
        # словарь имя:цена
        r = {list_names[name]: str(list_price[name]).replace(',', '') for name in range(len(list_price))}

        for trader in r.keys():
            if trader in conf.list_ignore or float(r[trader]) > conf.Hight:
                continue
            else:
                list_l.append(r[trader])
        if len(list_l) > 0:
            min_price = float(list_l[0])
            print(min_price)
            my_new_price = str(round(min_price + conf.Y, 2))
            params = {u'price_equation': my_new_price}
            try:
                conn = api.hmac(API_keys.hmac_key, API_keys.hmac_secret)
                a = conn.call('POST', conf.Me_3_1, params).json()
                print(a)
                del conn
            except Exception as e:
                print(e)
        time.sleep(6)