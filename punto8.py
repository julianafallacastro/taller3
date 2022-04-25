#Entradas
P=int(input("- "))
Q=int(input("- "))
#Caja Negra
r=P*3+Q*4-2*P*2
#Salidas
if r>680:
    print("P y Q satisfacen la expresión: ", r, "> 680")
else:
    print("P y Q no Satisfacen la expresión: ", r, "no es mayor a 680")