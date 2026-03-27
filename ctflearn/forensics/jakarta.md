Running the command
```bash
exiftool -v6 Jakarta.jpg
```
reveals an unknown trailer with an offset at the end of the output. Analyzing the image with HexEd, multiple FF D9 markers can be found that should be used as separators to split the trailer into parts. A Python program is a good choice for this purpose.
```python
with open('Jakarta.jpg', 'rb') as f:
  jpg = f.read()

trailer = jpg[0xC41E1:]
parts = trailer.split(b'\xff\xd9')
parts = parts[:-1]

for i, part in enumerate(parts):
  filename = f'part{i}.bin'
  with open(filename, 'wb') as f:
    f.write(part)
```
The program creates 4 different parts. Using a RSA key generator and counting it's bytes reveals that part0.bin is most likely an encrypted key. Opening up files part1.bin and part2.bin, it's easy to notice almost readable text, so it's very likely that the ROT cipher was used. Analyzing the files with CyberChef, it becomes clear ROT-(-1) was used. Once again, a Python program is a good choice for decryption.
```python
with open('part1.bin', 'rb') as f:
  data1 = f.read()

with open('part2.bin', 'rb') as f:
  data2 = f.read()

decoded1 = ''
for b in data1:
  decoded1 += chr(b - 1)

decoded2 = ''
for b in data2:
  decoded2 += chr(b - 1)

with open('xorFile.py', 'w') as f:
  f.write(decoded1)

with open('findOffset.py', 'w') as f:
  f.write(decoded2)

print('\n=== xorFile.py ===')
print(decoded1)
print('\n=== findOffset.py ===')
print(decoded2)
```
This program produces 2 Python programs that are meant to be used as hints for one final program that requires the previously found part0.bin encrypted key file.
```python
with open('Jakarta.jpg', 'rb') as f:
  jpg = f.read()

with open('part0.bin', 'rb') as f:
  encrypted_key = f.read()

rsa_prefix = b'-----BEGIN RSA PRIVATE KEY-----'

xor_bytes = []
for i in range(len(rsa_prefix)):
  xor_bytes.append(rsa_prefix[i] ^ encrypted_key[i])

offset = jpg.find(bytes(xor_bytes))

rsa_key = bytearray()
for i in range(len(encrypted_key)):
  rsa_key.append(encrypted_key[i] ^ jpg[offset + i])

with open('jakarta_rsa.key', 'wb') as f:
  f.write(rsa_key)
```
Finally, the last file part3.bin is used to decode the acquired key using the command
```bash
openssl rsautl -decrypt -inkey jakarta_rsa.key -in part3.bin -pkcs
```
that reveals the flag.
