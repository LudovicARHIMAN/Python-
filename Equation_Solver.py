from math import *

def recup_a(x):
    if x[0]=="-":
        a= int(x[1])
        s = -abs(a)
        return s

    if x[0]=="+":
        a = int(x[1])
        return a

    a= int(x[0])
    return a

def recup_b(x):
    for i in range(3):
        x = x[:-1]
    return recup_c(x)

def recup_c(x):

    if x[-2]=="+":
        c = int(x[-1])
        return c

    if x[-2]=="-":
        c = int(x[-1])
        x=-abs(c)
        return  x

def CalcRacine(a,b,c):
    delta = (b**2)-4*a*c

    if delta >0:
        racine1=(-(b)-sqrt(delta))/(2*a)
        racine2=(-(b)+sqrt(delta))/(2*a)
        return racine1, racine2, "sont solution de l'equation"

    if delta==0:
        return (-(b))/(2*a) , "est la solution à l'équation"

    if delta<0:
        return "l'equation n'admet pas de solution"

def resoudre_equation_2ndrg(x):
    equ=x.replace(" ","")
    a=recup_a(equ)
    b=recup_b(equ)
    c=recup_c(equ)
    return CalcRacine(a,b,c)

print(resoudre_equation_2ndrg("2x²-9x-5"))

