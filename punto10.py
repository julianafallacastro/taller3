#Entradas
c=int(input("Ingrese la categoría: "))
#Caja Negra
sb1=5000000*0.10+5000000
sb2=4300000*0.15+4300000
sb3=3600000*0.20+3600000
sb4=2000000*0.40+2000000
sb5=900000*0.60+900000
#Salidas
if c==1:
    print("Sueldo bruto: ", sb1)
elif c==2:
    print("Sueldo bruto: ", sb2)
elif c==3:
    print("Sueldo bruto: ", sb3)
elif c==4:
    print("Sueldo bruto: ", sb4)
elif c==5:
    print("Sueldo bruto: ", sb5)