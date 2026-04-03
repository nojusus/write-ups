Download the provided file "image.jpg" and run the command
```bash
binwalk -e image.jpg
```
to extract a hidden file "D0F0.zip". Go back to the first file and run the command
```bash
strings image.jpg | grep -A 1 pass
```
to get the password used to extract the found file. Convert the extracted file "bin" into a 600x600 grid with this Python program:
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
Open the exported file "flag.txt", zoom out, rotate it, and mirror it horizontally to get the flag.
