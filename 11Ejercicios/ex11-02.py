"""
PAQUETES EXTERNOS: uso de moviepy 1.0.3 (https://pypi.org/project/moviepy/)
moviepy es una librería open source que sirve para manipular ficheros de video.

Antes de nada, instalar la librería:
 a) File/Settings -> Project11: / Python interpreter / + -> buscamos moviepy 1.0.3 e instalamos
 b) vemos que se instalan todos los paquetes necesarios
 c) ya podemos seguir...

Tiene dos clases muy importantes:
 - VideoFileClip -> operaciones con video
 - AudioFileClip -> operaciones con audio
"""
from moviepy.editor import *

# abrimos el fichero con el que vamos a trabajar. Dura 9 seg
video = VideoFileClip("intro_canal.mp4")

# Obtenemos un subclip entre el segundo 4 y el 9. Dura 5 seg
clip = video.subclip(4, 9)

# Rotamos 180 el subclip
clip = clip.rotate(180)

# extraer el audio del clip
audio = clip.audio
audio.write_audiofile("audio.mp3")

# guardamos el subclip en otro fichero *.mp4
clip.write_videofile("resultado.mp4")

# guardamos el subclip en otro fichero *.webm
clip.write_videofile("resultado.webm")
