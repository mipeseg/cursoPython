"""
SINTETIZADOR DE VOZ con: pyttsx3 2.90 (https://pypi.org/project/pyttsx3/)
textToSpeech
"""
import pyttsx3  # importamos el modulo

engine = pyttsx3.init()  # creamos un objeto de la clase pyttsx3.engine.Engine

# VOICE RATE (VELOCIDAD DE LA VOZ)   lento < 200 < rapido
print("Voice rate:", engine.getProperty('rate'))   # 200 mostramos el voice rate actual (por defecto 200)
engine.setProperty('rate', 150)     # modificamos el voice rate a 125

# VOLUME (VOLUMEN  0=callado   1=hablar)
print(engine.getProperty('volume'))   # volumen actual (min=0 and max=1)   1 por defecto
engine.setProperty('volume', 1)       # configurando volumen

# VOICE (Femenina inglés = 0  Femenina español = 1)
voices = engine.getProperty('voices')       # genera una lista de todas las voces del sistema
print(voices[0])                            # voz femenina en español (HELENA)
print(voices[1])                            # voz femenina en inglés  (ZIRA)
engine.setProperty('voice', voices[0].id)   # changing index, changes voices. 1 for female

# SINTETIZAR VOZ (forma 1)
engine.say("Esto es una prueba de síntesis de voz")  # cargamos el texto en el objeto
engine.runAndWait()  # iniciamos la sintesis
engine.stop()  # detiene el objeto

# SINTETIZAR VOZ (forma 2)
pyttsx3.speak("Esta es la segunda prueba")

# GENERAL FICHERO DE AUDIO
engine.save_to_file("Hasta luego Lucas", 'test.mp3')
engine.runAndWait()
engine.stop()
