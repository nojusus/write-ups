Scanning the downloaded inception.png file's QR code, you get a hint that you need to look closer. Zooming into the image, you can find a lot of smaller QR codes inside the big one. Python is a good solution to avoid manually scanning each one. You can use this program.
```python
import cv2
import numpy as np
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode

img = "inception.png"
img_cv = cv2.imread(img)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
pil_img = Image.open(img)

small = cv2.resize(img_cv, None, fx=0.25, fy=0.25)
detector = cv2.QRCodeDetector()
outer_text, bbox, _ = detector.detectAndDecode(small)

pts = (bbox[0] * 4).astype(int)
x_start, y_start = pts[0][0], pts[0][1]
x_end,   y_end   = pts[2][0], pts[2][1]

modules = 21
mod_size = (x_end - x_start) / modules

chunks = []

for r in range(modules):
    for c in range(modules):
        x0 = x_start + int(c * mod_size)
        y0 = y_start + int(r * mod_size)
        x1 = x_start + int((c + 1) * mod_size)
        y1 = y_start + int((r + 1) * mod_size)

        cell = pil_img.crop((x0, y0, x1, y1))
        text = None

        for invert in [True, False]:
            for size in [400, 600, 800]:
                attempt = cell.convert("RGB")
                if invert:
                    attempt = ImageOps.invert(attempt)
                attempt = attempt.resize((size, size), Image.NEAREST)
                decoded = decode(attempt)
                if decoded:
                    text = decoded[0].data.decode('utf-8')
                    break
            if text:
                break

        if text:
            chunks.append((r, c, text))

message = ''.join(t for _, _, t in chunks)
print(message)
```
Running this program will reveal a base64 encoded string. Use the site https://base64.guru/converter/decode/image/png to convert the string into a PNG file. The PNG file will be another QR code that you will need to scan to obtain the flag.
