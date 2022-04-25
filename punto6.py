#Entradas
d=input ("Ingrese los datos A B C D: ")
a,b,c,d=d. split(" ")
a=str(a)
b=str(b)
c=str(c)
d=str(d)
#Caja Negra
n=int ( (a+b+c+d) )
c=int (c)
#Salidas
if (c>5):
    re=round (n,-2)
    print(re)
else:
    (c<5)
    re=int ( (round(n, -2)))
    print(re)