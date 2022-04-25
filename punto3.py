#Entradas
n=input()
(a,b,c,d)=n.split(" ")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
#Caja Negra
a=(a-c)**2
b=((a-b)**3)/d
#Salidas
if d==0:
    print(a)
elif d>0:
    print(b)