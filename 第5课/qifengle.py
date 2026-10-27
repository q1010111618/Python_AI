import numpy as np
import pygame
import time

pygame.mixer.init(frequency=44100)

# 音名 -> 频率
NOTE_FREQ = {
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
    'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25,
    'D5': 587.33, 'E5': 659.25, 'F5': 698.46, 'G5': 783.99,
    'A5': 880.00, 'B5': 987.77,
}

# 《起风了》主歌片段（简化，Gb/F#大调转成好写的中音区）
melody = [
    ('G4', 0.5), ('A4', 0.5), ('C5', 1.0), ('B4', 0.5), ('A4', 0.5),
    ('G4', 1.0), ('E4', 1.0),
    ('G4', 0.5), ('A4', 0.5), ('C5', 1.0), ('D5', 1.0),
    ('C5', 1.0), ('A4', 1.0),
]

def play_tone(freq, dur):
    sr = 44100
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    wave = 0.3 * np.sin(2 * np.pi * freq * t)
    wave = (wave * 32767).astype(np.int16)
    stereo = np.column_stack((wave, wave))
    sound = pygame.sndarray.make_sound(stereo)
    sound.play()
    time.sleep(dur)

for name, beat in melody:
    play_tone(NOTE_FREQ[name], beat)

pygame.mixer.quit()