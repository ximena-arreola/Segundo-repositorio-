#examen 4 
#ximena lizeeth sanchez arreola
# Pedir datos al usuario
numero_tabla = int(input("cual Número de la tabla deseas: "))
inicio = int(input("ingresa Número inicial: "))
tope = int(input("di tu Número tope: "))
intervalo = int(input("ingresa el Intervalo: "))

# ascendente
print("Tabla en forma ascendente:")
i = inicio
while i <= tope:
    print(numero_tabla, "x", i, "=", numero_tabla * i)
    i = i + intervalo

# descendente
print("Tabla en forma descendente:")
i = tope
while i >= inicio:
    print(numero_tabla, "x", i, "=", numero_tabla * i)
    i = i - intervalo