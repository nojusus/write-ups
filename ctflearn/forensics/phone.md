Download the provided file "phone.wav" and run this program:
```python
import wave
import numpy as np
from itertools import groupby

with wave.open('phone.wav', 'rb') as w:
    frames = w.readframes(w.getnframes())
    sr = w.getframerate()

samples = np.frombuffer(frames, dtype=np.int16).astype(np.float32)

ROW_FREQS = [697, 770, 852, 941]
COL_FREQS = [1209, 1336, 1477, 1633]

DTMF_TABLE = {
    (697, 1209): '1', (697, 1336): '2', (697, 1477): '3',
    (770, 1209): '4', (770, 1336): '5', (770, 1477): '6',
    (852, 1209): '7', (852, 1336): '8', (852, 1477): '9',
    (941, 1209): '*', (941, 1336): '0', (941, 1477): '#',
}

def detect_freq(chunk, target_freqs, sr):
    N = len(chunk)
    best_freq = None
    best_mag = 0
    for f in target_freqs:
        k = round(f * N / sr)
        n = np.arange(N)
        mag = abs(np.sum(chunk * np.exp(-2j * np.pi * k * n / N))) / N
        if mag > best_mag:
            best_mag = mag
            best_freq = f
    return best_freq, best_mag

window_size = int(sr * 0.04)
step = int(sr * 0.01)
raw_symbols = []

i = 0
while i + window_size < len(samples):
    chunk = samples[i:i+window_size]
    energy = np.mean(chunk**2)
    if energy > 100000:
        rf, rm = detect_freq(chunk, ROW_FREQS, sr)
        cf, cm = detect_freq(chunk, COL_FREQS, sr)
        if rm > 100 and cm > 100:
            raw_symbols.append(DTMF_TABLE.get((rf, cf), '?'))
        else:
            raw_symbols.append('_')
    else:
        raw_symbols.append('_')
    i += step

runs = [(sym, len(list(group))) for sym, group in groupby(raw_symbols)]
filtered = [(sym, dur) for sym, dur in runs if dur >= 3]
digits = [sym for sym, dur in filtered if sym != '_']

print(''.join(digits))
```
Copy the printed string and paste it inside the "seq" variable in this program:
```python
from PIL import Image

seq = ""

sections = seq.split('#')
header_bin = sections[0][6:]  # skip the 6-digit non-binary prefix
rows = [header_bin] + sections[1:-1]  # drop the trailer too

scale = 20
pad = 60
size = 25 * scale + pad * 2

img = Image.new('RGB', (size, size), 'white')
pixels = img.load()

for r, row in enumerate(rows):
    for c, bit in enumerate(row):
        color = (0, 0, 0) if bit == '0' else (255, 255, 255)
        for dy in range(scale):
            for dx in range(scale):
                pixels[pad + c*scale+dx, pad + r*scale+dy] = color

img.save('qr.png')
```
Run the program and scan the QR code to get the flag.
