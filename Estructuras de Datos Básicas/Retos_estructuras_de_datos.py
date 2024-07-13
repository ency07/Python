# Aquí tienes algunos retos para practicar lo que hemos visto.
# Te proporcionaré pistas para ayudarte sin darte la sintaxis exacta.

# ? Ejercicio 1: Números
# * Descripción
# Crea un programa que pida al usuario dos números y realice las siguientes operaciones: suma, resta, multiplicación, división y módulo. Muestra los resultados de cada operación.

# Pistas
# Usa input() para obtener los números del usuario.
# Recuerda convertir los inputs a números.
# Realiza las operaciones aritméticas básicas.
# Usa print() para mostrar los resultados.

# ? Ejercicio 2: Cadenas
# * Descripción
# Escribe un programa que tome una frase del usuario y realice las siguientes operaciones:

# Convierta la frase a mayúsculas.
# Convierta la frase a minúsculas.
# Cuente cuántas veces aparece una letra específica en la frase.
# Reemplace todas las ocurrencias de una palabra en la frase con otra palabra.

# Pistas
# Usa los métodos de cadenas (upper(), lower(), count(), replace()).
# Usa input() para obtener la frase y las palabras/letras del usuario.

frase = input("\nEscibe una frase y convirtamos las letras MAYUSCULAS: ")
Mayusculas = frase.upper()
print(Mayusculas)

frase = input("\nEscibe una frase y convirtamos las letras MINUSCULAS: ")
minusculas = frase.lower()
print(minusculas)

# Conteo de letra
frase = input("\nCuantas veces aparece la letra: ")
conteo = frase.count("e")
print(conteo)

# Conteo de letra desde usuario
frase = input("\nEscibe una frase y contemos una letra en especial: ")
letra = input("Cuantas veces aparece la letra: ")
conteo = frase.count(letra)
print(conteo)

# Remplazar letra por otra desde usuario
frase = input("\nEscibe una frase y remplacemos una letra: ")
letra1 = input("Que letra quieres remplazar: ")
letra2 = input("Por cual la quieres remplazar: ")

resultado = frase.replace(letra1, letra2)
print(resultado)

# TODO >>>>>>>>>  Ejercicio 2 Resuelto  <<<<<<<<<<<<

# Se aprendio :
# que .upper(), es para colcar las letras en mayusculas
# que .lower(), es para colocar las letras en minusculas
# que .count(), te contabiliza la cantidad de elementos o caracteres
# que .replace(), funciona con dos elementos, 1 el que quieres remplazar y 2 por el cual lo quieres remplazar

# TODO >>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<

# ? Ejercicio 3: Listas
# * Descripción
# Crea un programa que haga lo siguiente:

# Cree una lista con cinco números enteros.
# Añada un nuevo número al final de la lista.
# Inserte un número en la segunda posición.
# Elimine el tercer número de la lista.
# Ordene la lista en orden ascendente.
# Imprima la lista final.

# Pistas
# Usa los métodos de listas (append(), insert(), remove(), sort()).
# Recuerda que las listas se indexan desde 0.

lista = [9, 3, 0, 8, 12, 15, 10, 7]

lista.append(int(input("Añada un nuevo numero a la lista: ")))
print(f"Lista actualizada con el nuevo numero {lista}")

print("\nInsertaremos un numero en una posicion especifica\n")
insertar = int(input("En que posicion quieres insertar el numero: "))
num = int(input("Cual es el numero: "))
lista.insert(insertar, num)
print(f"Lista actualizada con el nuevo numero {lista} ")

print("\nAhora eliminaremos un numero: \n")
eliminar = int(input("En que posicion quieres eliminar el numero: "))
lista.pop(eliminar)
print(f"Lista actualizada con el metodo .pop {lista} \n")

lista.sort()
# nueva_lista = sorted(lista, reverse=True)
# print(nueva_lista)
print(lista)

# TODO >>>>>>>>>>  Ejercicio 3 Resuelto  <<<<<<<<<<<<
# Que se aprendio:
# que .insert(), es para insertar un elemento en una posicion especifica y que funciona con 2 elementos
# que .pop(), elimina la posicion que le asignes
# que .remove(), elimina el elemento quieres eliminar
# que .sort(), te organiza de forma ascendente la lista  ---- Para invertir se usa (reverse=True)
# tambien se puede utilizar el metodo =sorted(), para organizar la lista --- igual que arriba

# TODO >>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<

# ? Ejercicio 4: Tuplas
# * Descripción
# Crea una tupla con cinco elementos (pueden ser de diferentes tipos). Realiza las siguientes operaciones:

# Imprime el primer y el último elemento de la tupla.
# Intenta cambiar el segundo elemento y observa el error.
# Desempaqueta la tupla en variables individuales e imprime cada una.

# Pistas
# Recuerda que las tuplas son inmutables.
# Usa la indexación para acceder a los elementos.
# Desempaquetar es simplemente asignar los elementos de la tupla a variables separadas.


tupla = (1, "DOS", 5, "cuatro", 3, True)
#primer = tupla[1]


cero= tupla[0]
uno= tupla[1]
dos=tupla[2]
tres=tupla[3]
cuatro = tupla[4]
cinco = tupla[5]

#print(primer)

print(cero)
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

# ? Ejercicio 5: Diccionarios
# * Descripción
# Crea un diccionario para almacenar información de una persona (nombre, edad, ciudad).
# Realiza las siguientes operaciones:

# Añade una nueva clave-valor (por ejemplo, profesión).
# Modifica el valor de una clave existente.
# Elimina una clave-valor del diccionario.
# Imprime todas las claves y valores del diccionario.

# Pistas
# Usa los métodos del diccionario (update(), pop(), keys(), values()).
# Puedes usar input() para obtener información adicional del usuario.

# ? Ejercicio 6: Conjuntos
# *Descripción
# Crea un conjunto con cinco números enteros. Realiza las siguientes operaciones:

# Añade un nuevo número al conjunto.
# Elimina un número del conjunto.
# Verifica si un número específico está en el conjunto.
# Realiza la unión y la intersección con otro conjunto de números y muestra los resultados.
# Pistas
# Usa los métodos de conjuntos (add(), remove(), union(), intersection()).
# Recuerda que los conjuntos no permiten duplicados.

# ? Ejercicio 7: Booleanos
# *Descripción
# Escribe un programa que tome dos números del usuario y determine lo siguiente:

# Si ambos números son positivos.
# Si al menos uno de los números es negativo.
# Si los dos números son iguales.
# Si el primer número es mayor que el segundo.

# Pistas
# Usa operadores lógicos (and, or, not).
# Usa operadores de comparación (==, !=, >, <).

# ? Ejercicio Completo
# Combina varios de los conceptos anteriores en un programa que:

# Pida al usuario su nombre, edad y ciudad.
# Almacene esta información en un diccionario.
# Cree una lista con números del 1 al 10.
# Elimine los números pares de la lista.
# Añada los números restantes a un conjunto.
# Verifique si el número 5 está en el conjunto.
# Imprima todos los datos recolectados y manipulados.

# Pistas
# Usa input() para obtener datos del usuario.
# Usa bucles (for o while) para recorrer la lista.
# Usa estructuras condicionales (if).
# Utiliza diccionarios, listas y conjuntos según sea necesario.
