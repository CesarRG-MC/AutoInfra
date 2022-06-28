distancia = float(input("Igrese la distancia entre los dos vehiculos (Km): "))
velocidad1 = float(input("Ingrese la velocidad del primer vehiculo (Km/h): "))
velocidad2 = float(input("Ingrese la velocidad del segundo vehiculo (Km/h): "))
tiempo = (distancia) / (velocidad1 + velocidad2)

print("El tiempo de encuentro entre ambos vehiculos es de: ", round (tiempo, 2), " horas")