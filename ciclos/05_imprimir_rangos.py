#range() imprimir valores de un rango

#si range() recibe un parametro, se interpreta como el nomuero en donde termina el rango-1
for x in range(5):
    print(x)

#Si range() recibe dos parametros, se interpreta como:
#El primer parametro es el inicio
#El segundo parametro es donde termina el rango-1
for y in range(1,11):
    print(y)

#Si range() recibe tres parametros, se interpretara como:
#El primer parametro es el inicio
#El segundo parametro es donde termina el rango-1
#El tercer parametro es el incremento
for z in range(10,51,5):
    print(z)
    