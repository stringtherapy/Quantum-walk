octave = {'C4': 261.63,'D': 293.67 ,'E': 329.63, 'F': 349.23, 'G': 392.00, 'A': 440.00, 'B': 493.89, 'C5': 523.25}
note_duration = 0.5
samplerate = 44000
c_major = list(octave)

import numpy as np
from scipy.io.wavfile import write

def generate_note(freq, duration=note_duration):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t) 
    return wave

def get_song_data(music_notes):
    song = [generate_note(octave[note]) for note in music_notes.split(',')]
    song = np.concatenate(song)
    return song