"""
Fuente 1 --> https://www.youtube.com/watch?v=MYVWPmzsRz8
web autor Music21 --> https://web.mit.edu/music21/
documentacion Music21 --> https://web.mit.edu/music21/doc/index.html

Pasos a seguir si la librería music21 no puedes instalarla con pip:  pip install library21
 a) descargar el fichero music21-7.1.0.tar.gz (https://github.com/cuthbertLab/music21/releases/tag/v7.1.0)
 b) descomprimirlo
 c) creamos un proyecto en PyCharm. Nos pregunta si queremos conservar los ficheros. Decimos SI
 d) abrimos el fichero installer.py y lo ejecutamos
 e) Nos pide instalar una serie de librerias externas
 f) En caso que falle alguna (a mi me falla matplotlib) podemos entrar en Pypi unoffical y descargarla
    (https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib)
 g) En mi caso descargo "matplotlib‑3.4.3‑cp310‑cp310‑win_amd64.whl" y lo copia en mi proyecto "music21-7.1.0"
 h) Ahora ya puede ejecutar installer.py -> cuando acaba estara instalar la librería music21
 i) creamos un fichero main.py y escribirmos el siguiente código. Para aprovechar el potencial de la
    libreria Music21 se recomienda descargar e instalar el editor de partituras gratuito
    musescore (https://musescore.org/es). Una vez instalado hemos de configurar Music21
"""
from music21 import note, stream, configure, instrument, converter     # importamos los modulos note, stream y configure


# configure.run()  # configuramos Music21 para que reconozca Musescore (SOLO HACERLO UNA VEZ)

# creamos objetos de clase Note -> nota a interpretar en notación anglosajona y duración de la nota
# DO RE MI FA SOL LA SI  ( Notación musical latina)
# C  D  E  F  G   A  B   ( Notación musical anglosajona)

# PARTITURA DE EJEMPLO (SQUID GAME)
# Generamos las notas musciales
n1 = note.Note('B4', quarterLength=.5)  # corchea
n2 = note.Note('B4', quarterLength=.5)  # corchea
n3 = note.Note('B4', quarterLength=1)   # negra
n4 = note.Note('B4', quarterLength=.5)  # corchea
n5 = note.Note('B4', quarterLength=.5)  # corchea
n6 = note.Note('B4', quarterLength=1)   # negra
n7 = note.Note('D#5', quarterLength=.5) # corchea
n8 = note.Note('B4', quarterLength=.5)  # corchea
n9 = note.Note('B4', quarterLength=.5)  # corchea
n10 = note.Note('A4', quarterLength=.5) # corchea
n11 = note.Note('G4', quarterLength=.5) # corchea
n12 = note.Note('A4', quarterLength=.5) # corchea
n13 = note.Note('B4', quarterLength=1)  # negra

n14 = note.Note('B4', quarterLength=.5) # corchea
n15 = note.Note('B4', quarterLength=.5) # corchea
n16 = note.Note('B4', quarterLength=1)  # negra
n17 = note.Note('B4', quarterLength=.5) # corchea
n18 = note.Note('B4', quarterLength=.5) # corchea
n19 = note.Note('B4', quarterLength=1)  # negra
n20 = note.Note('B4', quarterLength=.5) # corchea
n21 = note.Note('A4', quarterLength=.5) # corchea
n22 = note.Note('G4', quarterLength=.5) # corchea
n23 = note.Note('A4', quarterLength=.5) # corchea
n24 = note.Note('G4', quarterLength=.5) # corchea
n25 = note.Note('E4', quarterLength=.5) # corchea
n26 = note.Note('E4', quarterLength=1)  # negra

s = stream.Stream()  # s es el contenedor de cualquier objeto que herede de la clase Music21Objects
s.append([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16,
          n17, n18, n19, n20, n21, n22, n23, n24, n25, n26]) # añadimos una lista de objetos nota al contenedor

s.show("text")  # muestra el contenido del stream en pantalla
s.show("musicxml")  # muestra el contenido del stream como partitura abriendo MuseCore
s.write("midi", fp="SquidGame_piano.mid")  # genera un fichero midi

# Leemos un fichero MIDI, cambiamos el sonido del instrumento de cada nota y generamos otro fichero MIDI
st = converter.parse("SquidGame_piano2.mid")  # cargamos el fichero MIDI en un stream
for nota in st.recurse():
    if 'Instrument' in nota.classes:  # or 'Piano'
        nota.activeSite.replace(nota, instrument.Flute())  # sonido de flauta

st.write('midi', 'SquidGame_PanFlute.mid')  # creamos otro fichero midi
