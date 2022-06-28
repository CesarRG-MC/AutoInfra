from calendar import isleap

año = int(input("Ingrese un año: "))

if isleap(año):
    print(año, " es año biciesto")
else:
    print(año, " no es año biciesto")