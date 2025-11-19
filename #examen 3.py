#examen 3 
#ximena lizeeth sanchez arreola 
pares = 0
impares = 0
nulos = 0
suma = 0


for i in range(5):
    numero = int(input("Ingresa un número preferido : "))
    suma += numero

    if numero == 0:
        nulos += 1
    elif numero % 2 == 0:
        pares += 1
    else:
        impares += 1


print("\nResultados:")
print("la Cantidad de números pares:", pares)
print(" esta fue la Cantidad de números impares:", impares)
print(" ijole esta fue la Cantidad de números nulos (0):", nulos)
print("Suma total de los números ingresados:", suma)