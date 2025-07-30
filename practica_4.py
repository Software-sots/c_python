
#calculadora con una sola variables
print("calculadora con una sola variable")

print("******************************")
print("menu de opciones")
print("******************************\n")

print(" 1. Suma\n", "2. Resta\n", "3. multiplicacion\n", "4. Division\n", "5. Division entera\n","6. Exponente\n", "7. Modulo" )

numero=int(input("\nintroduce la opcion deseada: "))

if numero == 1:
    print("Elegiste suma")
    numero = int(input("\nintroduce el primer numero: "))
    numero += int(input("\nintroduce el segundo numero: "))
    print("el resultado de la suma es ",numero )

elif numero == 2:
    print("Elegiste resta")
    numero = int(input("\nintroduce el primer numero: "))
    numero += int(input("\nintroduce el segundo numero: "))
    print("el resultado de la resta es ",numero )

elif numero == 3:
    print("Elegiste Multiplicacion")
    numero = float(input("\nintroduce el primer numero: "))
    numero *= float(input("\nintroduce el segundo numero: "))
    print("el resultado de la multipicacion es ",round(numero,2 ))

elif numero == 4:
    print("Elegiste Division")
    numero = float(input("\nintroduce el primer numero: "))
    numero /= float(input("\nintroduce el segundo numero: "))
    print("el resultado de la division es ",round(numero,2 ) )

elif numero == 5:
    print("Elegiste Division entera")
    numero = int(input("\nintroduce el primer numero: "))
    numero //= int(input("\nintroduce el segundo numero: "))
    print("el resultado de la division entera es ",numero )

elif numero == 6:
    print("Elegiste Exponente")
    numero = int(input("\nintroduce el primer numero: "))
    numero **= int(input("\nintroduce el segundo numero: "))
    print("el resultado de la multipicacion es ",numero )

elif numero == 7:
    print("Elegiste Modulo o residuo")
    numero= float(input("\nintroduce el primer numero: "))
    numero %= float(input("\nintroduce el segundo numero: "))
    print("el residuo es  es ",round(numero,2 ))

else:
    print("Opcion no valida")























