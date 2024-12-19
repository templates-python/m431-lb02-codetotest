from dataclasses import dataclass as __A
from datetime import datetime as __D
from typing import Optional as __O

def __M():
    __g = __m()
    __z(__g)
    __r(__g)

def __m():
    __f = dict()
    for __p in ['Marco', 'Bernd', 'Adam']:
        __f[__p] = list()
    return __f

def __z(__h):
    __q = input('Kundenname > ')
    __y = True
    while __y:
        __e = __X()
        __h[__q].append(__e)
        __l(__e)
        __y = input('Weitere Bezüge (y/N) > ') == 'y'

def __l(__E):
    __E.__s = __w('Start des Ladevorgangs')
    __E.__d = __w('Ende des Ladevorgangs')
    __E.__u = __w('Freigabe der Säule')
    __E.__n = __t('Strommenge in KWh >')

def __r(__i):
    for __c, __j in __i.items():
        if len(__j) > 0:
            __x = 0
            print(f'Abrechnung für {__c}')
            for __G in __j:
                print(f'  + {__G.__s.strftime("%d.%m.%Y %H:%M")}: CHF {__G.__v:.2f}')
                __x += __G.__v
            print(f'Total: CHF {__x:.2f}')

def __t(__o):
    __B = None
    while __B is None:
        try:
            __B = float(input(__o + ' > '))
            if __B <= 0:
                print('Geben Sie eine positive Zahl ein')
                __B = None
        except ValueError:
            print('Geben Sie eine positive Zahl ein')
    return __B

def __w(__W):
    __Z = None
    while __Z is None:
        __Y = input(__W + '(dd.mm.jjjj hh:mm) > ')
        try:
            __Z = __D.strptime(__Y, '%d.%m.%Y %H:%M')
        except ValueError:
            print('Geben Sie ein gültiges Datum/Uhrzeit ein')
    return __Z

@__A
class __X:
    __s: __O[__D] = None
    __d: __O[__D] = None
    __u: __O[__D] = None
    __n: __O[float] = None

    @property
    def __v(self):
        __K = self.__n * 0.35
        __R = self.__u - self.__d
        __L = __R.total_seconds() / 60
        if __L > 15:
            __K += (__L - 15) * 0.05
        return round(__K, 2)

if __name__ == '__main__':
    __M()
