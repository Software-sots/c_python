#comparacion de numeros

print("programa para determiar cual es el numero mas grande")

num_1 = int(input("introduce el primer numero "))
num_2 = int(input("introduce tu segundo numero"))
num_3 = int(input("introduce tu tercer numero"))

if num_1  > num_2  and num_1   > num_3 :
    print(num_1," es el mayor")
else:
    if num_2 > num_3 :
        print(num_2, " es el mayor")
    else:
        print(num_3, " es el mayor")



