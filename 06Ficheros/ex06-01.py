"""
Hasta ahora estamos trabajando con objetos almacenados en memoria RAM (Volátil). Si queremos almacenar
duraderamente los datos, los tenemos que guardar en ficheros. Existen ficheros de distinto tipo, según como
codificamos la información (de texto, binarios...). En este curso veremos los más sencillos: LOS FICHEROS DE TEXTO

Cuando habla de ficheros de texto no es necesariamente deben tener *.txt. Puede ser *.csv o incluso una inventada
por nosotros, lo importante es que la codificación se ASCII/Unicode

En este curso veremos las operaciones de Apertura, Lectura, Escritura y Cierre de ficheros de texto

APERTURA
  - fichero = open(file,mode) -> FileHanding
    file: cadena con la ruta y nombre del fichero a abrir
    mode: modo de apertura
       "r":  read - Valor default. Abre un fichero en modo lectura. Da error si el fichero no existe
       -------------
       "a" - append - Abre un fichero existente en modo adición. Si no existe lo crea
       "w" - write - Abre un fichero en modo escritura. Si existe lo machaca. Si no existe lo crea
       "x" - create - Crea un fichero. Si existe da error.
    NOTA: Devuelve un FileHanding o manejador de fichero que debemos de conservar en una variable
LECTURA
 - fichero.read() -> lee el contenido entero del fichero
 - fichero.readline() -> lee la 1ª linea del fichero. Si lo volvemos a usar la 2ª y asi hasta que devuelva
                         " ", que significa que hemos llegado al final del fichero
 - fichero.readline(num) -> lee cierto nº de caracteres
 - fichero.readlines() -> devuelve una lista con todas las lineas del fichero de texto
ESCRITURA
 - fichero.write(cad) -> escribe en una cadena en un fichero de texto
 - fichero.writelines(lista) -> escribe una lista en un fichero de texto
CIERRE
  Aunque Python acaba cerrandolo automáticamente, lo ideal, es que cuando hemos terminado de operar
  con el fichero lo cerremos.

     - fichero.close()
"""

# LECTURA DE FICHEROS DE TEXTO
fichero = open("ficheros\\ex06-01.txt", "r")     # NOTA: ponemos \\ pq se piensa que es una secuencia de escape
print(fichero.read())   # muestra todas las líneas
fichero.close()

print()

fichero = open("ficheros\\ex06-01.txt", "r")
print(fichero.readline(), end="")  # linea 1
print(fichero.readline(), end="")  # linea 2
print(fichero.readline(), end="")  # linea 3
print(fichero.readline(), end="")  # linea 4
print(fichero.readline(), end="")  # error ¿? NO
fichero.close()

print("\n")  # salto de linea manual

fichero = open("ficheros\\ex06-01.txt", "r")
print(fichero.readline(3))  # lin
print(fichero.readline(1))  # e
print(fichero.readline(3))  # a 1
fichero.close()

print("\n")

fichero = open("ficheros\\ex06-01.txt", "r")
lineas = fichero.readlines()
print(lineas)                  # ['línea 1\n', 'línea 2\n', 'línea 3\n', 'línea 4']
for linea in lineas:           # podemos iterar la lista para mostrar sus elementos
    print(linea, end="")

# ESCRITURA DE FICHEROS DE TEXTO
fichero = open("ficheros\\pruebas.txt", "w")   # si no existe lo crea. Si existe lo machaca
fichero.write("Contenido a escribir")
fichero.close()

fichero = open("ficheros\\pruebas.txt", "a")   # si no existe lo crea. Si existe añade al final
fichero.write("Mas contenido a escribir")
fichero.write("\nSigo escribiendo")
fichero.close()

# escritura de una lista en un fichero
fichero = open("ficheros\\frutas.dodo", "w")   # si no existe lo crea. Si existe lo machaca
lista = ["Manzana", "Pera", "Plátano"]  # lista que queremos guardar
for linea in lista:  # leemos cada elemento de lista y lo escribirmos en el fichero
    fichero.write(linea + "\n")
fichero.close()

# adicionamos otras lista al fichero frutas
fichero = open("ficheros\\frutas.dodo", "a")   # si no existe lo crea. Si existe añade
lista2 = ["Fresa", "Mora"]  # lista que queremos guardar
lista3 = ["\nPiña", "\nLima", "\nAguacate"]  # lista que queremos guardar
fichero.writelines(lista2)   # añadimos la lista entera
fichero.writelines(lista3)   # añadimos la lista entera
fichero.close()

print("\n")

# leemos el fichero frutas.dodo
fichero = open("ficheros\\frutas.dodo", "r")   # abre en modo lectura. Si no existe da error
lista4 = fichero.readlines()
print(lista4)
for c in lista4:
    # print(c, "-", end="")
    if c[-1] == "\n":
        print("%s - " % (c[0:len(c)-1]), end="")
    else:
        print("%s " % (c[0:len(c)]), end="")
fichero.close()
