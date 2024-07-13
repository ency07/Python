# Hoja de ruta detallada para aprender Python paso a paso - básico hasta lo avanzado.

# * Sintaxis Basica de Python

# TODO *** COMENTARIOS DE UNA LINEA
# print("Aprendiendo Python")  # Esto imprime un saludo


# TODO *** COMENTARIOS DE VARIAS LINEAS :
# Son 3 comillas (simples o dobles) al inicion y 3 comillas al final

"""
Son 3 comillas (simples o dobles) al inicion y 3 comillas al final-
Este es un comentario de varias lineas, ya que se puede dar saltos de lineas
para hacer comentarios mas extensos y explciacion del codigo
"""
print("Aprendiendo Python")

# TODO *** IDENTACION
# Es muy importante, porque se utilza para definir la estructura del codigo.
# Python no usa {} para delimitar bloques de codigo. En su lugar utiliza la identacion.

# * Cada bloque de codigo debe estar identado con la misma cantidad de espacios. Generalmente se usan 4 espaciios (una tabulada)

if 5 > 2:
    print("5 es mayor que 2")  # primer identado

    if 3 > 1:
        print("3 es mayor que 1")  # dentro del bloque del if anidaddo, segundo identado


# TODO ***  QUE ES UNA VARIABLES
# son espacio de memoria donde se almacenan datos.

# Asignacion de variables

x = 5
nommbre = "Juan"

# TODO *** TIPOS DE DATOS

# * Numeros, Cadenas (strings), Listas, Tuplas, Diccionarios, Conjuntos (sets), Booleanos.


# ? Numeros: python maneja diferentes tipos de numeros;

# Enteros (Int)  -- Sin decimales
num1 = 12

# Flotantes (float)  -- Con decimales
num2 = 12.1

# Numero Complejo   --
num3 = 3 + 4j

print(num1, num2, num3)

# ? Operaciones basicas
print("Operaciones basicas\n")
suma = 7 + 6
resta = 7 - 6
multiplicacion = 7 * 6
division = 7 / 6

# ? Operaciones avanzadas

potencia = 7**6
raiz_cuadrada = 7**0.5
modulo = 7 % 3

print(raiz_cuadrada)


# ? Cadenas (string)

cadena1 = "Aprendiendo"
cadena2 = "PYTHON"

# Concatenacion de cadenas
concatenar = cadena1 + " " + cadena2
print(concatenar)

# Repeticiones
repetir = "repetir! " * 3
print(repetir)


# Indexacion y slicing
letra = cadena1[1]
parte = cadena2[2:6]
print(letra)
print(parte)

# Metodos de cadena
mayusculas = cadena1.upper()
minusculas = cadena2.lower()
longitud = len(cadena1)
reemplazar = repetir.replace("r", "P")
print(mayusculas)
print(minusculas)
print(longitud)
print(reemplazar)


# ? Listas: Colecciones ordenadas y mutables de elementos, se definen usaso [].

# una lista de elementos
lista = [1, 2, 3, 4, 5]
mixta = [1, "dos", 3, 4, "cinco"]
print(f"Lista de numeros {lista}")
print(f"Lista mixta {mixta}")


# accediendo a elementos
print(f"Accediendo a los elementos de la lista -->:", lista[0])  # muestra el numero 1 de la lista
print(f"Accediendo a elementos de la lista mixta -->", mixta[4])


# Modificacion de elementos
primero = lista[0] = 10
mixta[1] = 'Quince'
penultimo = mixta[-2]

print(f"Modificacion de elementos de la lista --> {primero}")
print(f"Modificacion de elementos de la lista mixta --> {mixta}")
print(f"Modificacion de elementos de la lista mixta --> {penultimo}")


# Añadir elementos
lista.append(6)     # añade numero al final
lista.insert(1, 1.5)
print(f"Añadir elementos a la listas {lista}")

# eliminar elementos
lista.remove(3)
del lista[2]
lista = [1, 2, 3, 4, 5]
pop_elemento = lista.pop(0)

print(lista)  # se imprime la lista final con todas las modificaciones
print(mixta)  # se imprime la lista final con todas las modificaciones


# ? Tuplas: Colecciones ordenadas e inmutables de elementos. Se definen usando ().

tupla = (1, 2, 3, 'Cuatro', 5)

# Accediendo a los elemtos
primero = tupla[0]
ultimo = tupla[-1]

# desempaquetado de tuplas
a,b,c,d,e = tupla 

# Metodos de tuplas
longitud = len(tupla)
conteo = tupla.count (2)
indice = tupla.index('Cuatro')

print(primero)
print(ultimo)
print(a,b,c,d,e) # si falta un elemento manda error, misma cantidad de variables, misma cantidad de elementos
print(longitud)
print(conteo)
print(indice)

# A las tuplas no se le pueden modificar los elementos.
# tupla[0] = 10 --> esto ocasiona un error


# ? Diccionarios: Son colecciones de pares(clave-valor), estos se definen usando {}.

diccionario = {"nombre": "juan", "edad": 40, "ciudad": "Barranquilla"}

# Accediendo a valores
print(diccionario["nombre"])

# Modificando de valores
diccionario["edad"] = 25


# Añadir nuevas claves y valores a los diccionarios
diccionario["profesion"] = "Web Developer"

# Eliminar Pares, Claves-Valor
del diccionario["ciudad"]
print(diccionario)


# Metodos de diccionarios
claves = diccionario.keys() 
valores = diccionario.values()
items = diccionario.items()
diccionario.update({'profesion': 'Graphic Designer'}) # Añadir nuevas claves y valores a los diccionarios

print(items)


# ? Conjuntos (sets): Son colecciones desordenadas de elementos unicos. Se definen usando llaves {} o la funcion set().

conjunto = {1, 2, 3, 4, 5}

# Añadir elementos a las sets
conjunto.add(6)

# Eliminar elementos de los sets
conjunto.remove(1)

# No permite duplicados
conjunto.add(2)

print(conjunto)

# ? Booleanos: Representan valores de verdad; True y False

es_verdad = True
es_falso = False

print(es_verdad and es_falso)
print(es_verdad or es_falso)
print(not es_verdad)

#Probando los Booleanos


