from datetime import *
import requests
import time
import threading
import conf
import api
import API_keys


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
        for proxy in conf.proxy1:
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
                    print(proxy, end="  ")
                    min_price = float(list_l[0])
                    my_new_price = str(round(min_price - conf.X, 2))
                    params = {u'price_equation': my_new_price}
                    try:
                        a = api.hmac(API_keys.hmac_key, API_keys.hmac_secret, proxy={'https':conf.proxy_logpas + proxy}).call('POST', conf.Me_3, params).json()
                        print(a)
                    except Exception as e:
                        print(e)




def first_mess():
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
                d1 = str('/api/notifications/mark_as_read/' + d + '/')
                k = str(e['contact_id'])  # id сделки
                k1 = str('/api/contact_message_post/' + k + '/')

                # Mess_2 = 'Contact #' + k + ' payment marked complete'

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
        time.sleep(3)
        print('идем далше')
