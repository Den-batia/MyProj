import Cena

r = {}
price = 0


class Tm:
    def a(self, time, map):
        global price, r
        r = map
        price = (price + time) / 2


tm = Tm()
a = Cena.Cena('134.0.116.135:3128', tm)
a.start()

a.join()
print(a.is_alive())
print(a)
print(price)
print(r)

