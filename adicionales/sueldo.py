sueldo = float(input("Ingrese el sueldo del trabajador: "))
porcentaje = (15 * sueldo) / 100
aumento = sueldo + porcentaje

if sueldo <= 1000:
    print("Tuviste un aumento del 15%, tu sueldo ahora es: ", aumento)
else:
    print("Tu sueldo actual es mayo a $1000, no recibes aumento")
