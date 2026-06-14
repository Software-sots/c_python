# ejercicio práctico No. 6 
# Desarrollar un programa que elimine una palabra que forme parte de una cadena de caracteres.
# requerimientos indispensables 
#   - la cadena de caracteres deberá ser solicitda desde teclado
#   - la palabra a elminar debera ser solicitada desde teclado


string = input(str(" introduce una frase: "))
palabra = input(str(" introduce la palabra que deseas eliminar: ")) 

substring = " "
indice = string.find(palabra)
substring = string[ 0:indice] + string[indice + len(palabra):]

print(f"cadena resultante:{substring}")





