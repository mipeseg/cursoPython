"""
MUSIC21
https://www.youtube.com/watch?v=MYVWPmzsRz8
KEYBOARD 0.13.5 -> https://pypi.org/project/keyboard/
"""

import time
import keyboard   # nos permite detecta pulsaciones de teclas, entre otras muchas funciones

t = 0
while True:
    if keyboard.is_pressed('s'):
        print('se presionó [p]arar!')
        break
