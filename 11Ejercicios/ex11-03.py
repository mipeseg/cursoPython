"""
PAQUETES EXTERNOS: uso de melodia 1.1 (https://pypi.org/project/melodia/)
un chord o acorde es una combinación de 3 o más notas diferentes que suena a la vez
- Sistema musical nomenclatura latina:       do, re, mi, fa, sol, la, si
- Sistema musical nomenclatura anglosajona:  C, D, E, F, G, A, H
- En el piano hay 0 .. 7 octavas   (graves a agudas)
"""
from melodia.core.track import Track   # importamos la clase Track
from melodia.music import chord        # importamos el módulo chord
from melodia.io import midi            # importamos el módulo midi

track = Track(signature=(4, 4))     # creamos una pista o track con un compás 4x4

# añadimos distintos tipos acordes al track.   chord.tipo_acorde("nota base", duración, velocidad)
track.add(chord.maj('C3', (1, 1)))
track.add(chord.maj('D3', (1, 1)))
track.add(chord.min('A3', (1, 1)))
track.add(chord.maj7('G3', (1, 1)))

track.add(chord.maj('C1', (1, 1)))
track.add(chord.maj('D1', (1, 1)))
track.add(chord.min('A1', (1, 1)))
track.add(chord.maj7('G1', (1, 1)))

with open('chords.mid', 'wb') as f:   # guardamos el track en un fichero midi
    midi.dump(track, f)
