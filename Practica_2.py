
#Desarrollar un programa que solicite un numero entero desde el teclado al usuario,
# posteriormente, el programa debera determinar e indicar a traves de un mensaje,
# si el numero introducido es par o impar

# requerimentos el mensaje ne pantalla debera mostrar "la frase el numero es par o impar"
#junto con el numero que el ususario introdujo desde teclado

print("programa pasa conocer si un numero es para o impar")

numero =int(input("escribe un numero ") )

num2 = numero % 2

if num2 == 0 :
    print(" el numero", numero, " es par")
else:
    print("el numero",numero, " es impar")







