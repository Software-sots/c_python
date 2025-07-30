
print(" conjuncion")

num_uno=int(input("Escriba un numero mayor a 2 y menor que 5 ") )
if num_uno > 2 and num_uno <  5 :
    print("el numero",num_uno," cumple la condicion ")
else:
    print("el numero", num_uno, " No cumple la condicion ")


# disyuncion

print ("Disyuncion")
palabra = input("para cumplir con la condicion escribe si o yes ")
palabra=palabra.lower()

if palabra == "si" or palabra == "yes" :
    print("La condicion se cumple")
else:
    print("La condicion no se cumple")

print("negacion")
print("")

numero= int(input("introduce un numero igual a 5"))

if not numero ==5 :
    print("La condicion se cumple")

else:
    print("La condicion no se cumple")

