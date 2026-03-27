Running the command
```bash
file image.jpg
```
provides a base64 encoded string, that can be decoded with
```bash
echo "NjAweDYwMF9waWN0dXJl" | base64 -d
```
that provides a clue on how to obtain the flag. Running the command
```bash
binwalk image.jpg
```
shows that there are files hidden inside the image, and extracting them using
```bash
binwalk -e image.jpg
```
acquires a zip file that requires a password to extract. The password can be found going back to the image and running the command
```bash
strings image.jpg | grep -A 1 "pass"
```
The zip file extracts a "bin" file that contains a long line of binary numbers. This is where the clue found at the beginning comes into play, since the long string needs to be read like an image. A Python program is a good choice for this purpose.
```python
data = open('bin', 'rb').read()

with open('flag.txt', 'wb') as fd:
  for i in range(0, len(data), 600):
    if data[i] == 0x10:
      break
    if b'1' in data[i:i+600]:
      fd.write(data[i+200:i+364])
      fd.write(b'\n')
```
Running this command will produce the flag in text format that can be read like an image by zooming out.
