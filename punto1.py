#Entradas
c=float(input("Capital: "))
p=float(input("Porcentaje de interés: "))
#Caja Negra
r=round(c*p/100,2)
#Salidas
if r>100000:
    print("Interés reinvertido: ", r)
    c=round(c+r,2)
    print("Nuevo capital: ",c)
    print("Nuevo interés: ",round(c*p/100,2))
else:
    print("Interés no reinvertido: ",r)
