import math

def pgcd(a,b):
    while b:
        a, b= b, a%b
        return a

def ppcm(a,b):
    return abs(a*b)//pgcd(a,b)
def pair_ou_impair(n):
    return "pair" if n% 2 ==0 else "impair"

a=int(input("entrez le premier nombre"))
b=int(input("entrez le second nombre"))
print("pgcd de ",a,"et de ",b,"est:",pgcd(a,b))
print("ppcm de",a,"et de ",b,"est:",ppcm(a,b))
print( a ,"est",pair_ou_impair(a),"et ",b,"est",pair_ou_impair(b))

input()
