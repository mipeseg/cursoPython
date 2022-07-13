"""
SPEECH TO TEXT (Reconocimiento de voz y conversión a texto)
Fuente 1 -> https://www.youtube.com/watch?v=4srj2_J3j4E
Fuente 2 -> https://www.youtube.com/watch?v=9GJ6XeB-vMg
Fuente 3 -> Ejemplos -> https://github.com/Uberi/speech_recognition#readme

Librerías necesarias:
 - SpeechRecognition 3.8.1 -> https://pypi.org/project/SpeechRecognition/
 - PyAudio 0.2.11 (Oficial) -> https://pypi.org/project/PyAudio/
   NOTA: PyAudio dejo de revisarse en la version Python 3.6. Si provoca errores en la instalación
         hacer lo siguiente
         a) en el terminal escribir >>> python -> y muestra lo siguiente
            Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
            Type "help", "copyright", "credits" or "license" for more information.
         b) nuestra version es de 64 bit
         c) Vamos a la web www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio, un repositorio de librerías no
            oficial y descargamos "PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl", que es la version 64 bits
            para Python 3.10
         d) El fichero "PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl" lo copiamos en la carpeta de nuestro proyecto
         e) desde el terminal de PyCharm escribimos: pip install PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl
         f) Debería instalar PyAudio sin problemas. Despues en settings lo podemos comprobar

- PyAudio nonoficial -> https://www.youtube.com/watch?v=UiPGi-Ewb2c
                      https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
"""

import speech_recognition   # importamos el módulo

recognizer = speech_recognition.Recognizer()   # creamos el objeto recognizer

while True:  # bucle infinito
    try:  # código que puede que produzca errores
        with speech_recognition.Microphone() as mic:   # creamos el objeto micro que representa al microfono
            # reducimos el ruido ambiental haciendo que si no hablamos el sistema espera. En el momento se habla
            # continua con la siguiente instruccion
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            # Graba de una fuente de audio (el micro en este caso) y lo almacena en un objeto de clase AudioData
            # que devuelve
            audio = recognizer.listen(mic)

            # Realiza el reconocimiento de voz en un objeto de clase AudioData , utilizando la API de
            # reconocimiento de voz de Google. Después lo transcribe a texto
            # lista de lenguajes reconocidos
            # https://stackoverflow.com/questions/14257598/
            # what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134

            text = recognizer.recognize_google(audio)  # reconoce el inglés norteamericano
            # text = recognizer.recognize_google(audio, language="es-ES")  # reconoce el español de España
            if text.lower() == "bye-bye" or text.lower() == "adios":
                print(f"Reconocido: {text.lower()}")
                exit(0)  # terminamos el programa
            else:
                print(f"Reconocido: {text.lower()}")  # mostramos el texto en minúsculas

    except Exception as e:  # si se produce cualquier excepción ...
        recognizer = speech_recognition.Recognizer()  # volvemos a crear el objeto recognizer
        # continue
        # pass
