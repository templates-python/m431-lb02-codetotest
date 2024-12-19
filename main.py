from dataclasses import dataclass as AAA
from datetime import datetime as DDD
from typing import Optional as OOO

def MMM():
    ggg = mmm()
    zzz(ggg)
    rrr(ggg)

def mmm():
    fff = dict()
    for ppp in ['Marco', 'Bernd', 'Adam']:
        fff[ppp] = list()
    return fff

def zzz(hhh):
    qqq = input('Kundenname > ')
    yyy = True
    while yyy:
        eee = XXX()
        hhh[qqq].append(eee)
        lll(eee)
        yyy = input('Weitere Bezüge (y/N) > ') == 'y'

def lll(Eee):
    Eee.sss = www('Start des Ladevorgangs')
    Eee.ddd = www('Ende des Ladevorgangs')
    Eee.uuu = www('Freigabe der Säule')
    Eee.nnn = ttt('Strommenge in KWh >')

def rrr(iii):
    for ccc, jjj in iii.items():
        if len(jjj) > 0:
            xxx = 0
            print(f'Abrechnung für {ccc}')
            for GGG in jjj:
                print(f'  + {GGG.sss.strftime("%d.%m.%Y %H:%M")}: CHF {GGG.vvv:.2f}')
                xxx += GGG.vvv
            print(f'Total: CHF {xxx:.2f}')

def ttt(ooo):
    BBB = None
    while BBB is None:
        try:
            BBB = float(input(ooo + ' > '))
            if BBB <= 0:
                print('Geben Sie eine positive Zahl ein')
                BBB = None
        except ValueError:
            print('Geben Sie eine positive Zahl ein')
    return BBB

def www(WWW):
    ZZZ = None
    while ZZZ is None:
        YYY = input(WWW + '(dd.mm.jjjj hh:mm) > ')
        try:
            ZZZ = DDD.strptime(YYY, '%d.%m.%Y %H:%M')
        except ValueError:
            print('Geben Sie ein gültiger Datum/Uhrzeit ein')
    return ZZZ

@AAA
class XXX:
    sss: OOO[DDD] = None
    ddd: OOO[DDD] = None
    uuu: OOO[DDD] = None
    nnn: OOO[float] = None

    @property
    def vvv(self):
        KKK = self.nnn * 0.35
        RRR = self.uuu - self.ddd
        LLL = RRR.total_seconds() / 60
        if LLL > 15:
            KKK += (LLL - 15) * 0.05
        return round(KKK, 2)
if __name__ == '__main__':
    MMM()
