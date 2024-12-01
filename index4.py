def pgcd(a,b):
    while b != 0 :
        a, b = b, a % b
    return a 
            

a=int(input("entrez le premier entier"))
b=int(input("entrez le second entier"))
c = pgcd(a,b)
print("le pgcd de",a,"et de ",b,"est",c)
input()
