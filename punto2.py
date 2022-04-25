#Entradas
s=float(input("Salario bruto en COP: "))
#Caja Negra
a=s*0.15
s=s*0.15+s
a2=s*0.12
s2=s*0.12+s
#Salidas
if s<900000:
    print("Aumento: ", a)
    print("El sueldo total es: ", s)
else:
    print("Aumento: ", a2)
    print("El sueldo total es: ", s2)