#examen 2 
#ximena lizeeth sanchez arreola
# Pedir nombre y edad al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print(nombre, "si es mayor de edad.")
    print("Números que anteceden a tu edad en forma descendente:")
    
    for i in range(edad - 1, 0, -1):
        print(i)

else:
    print(nombre, "ijole es menor de edad.")
    suma = 0
    for i in range(1, edad):
        suma += i
    print("La suma de los números que anteceden a tu edad es:", suma)