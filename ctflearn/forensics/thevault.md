Extracting the zip file "TheVault.zip", 4 files are acquired. The readme file provides some context but no real hints. Running the command
```bash
strings Vault.jpg
```
and scrolling to the top of the output, a fake flag and 2 actual hints can be found. We know that it's necessary to use printable ASCII characters with a ROT cipher. Analyzing the image file in HexEd, multiple FF D9 markers can be found which signify hidden data. Locate the first FF D9 marker and export all the bytes after it as a new image. All that's left to do is to take in printable ASCII characters and brute force the ROT cipher to locate the flag. A Python program is a good solution for this purpose.
```python
data = open('bytes.jpg', 'rb').read()

printable = [b for b in data if 32 <= b <= 126]

for shift in range(95):
  decoded = ""
  for b in printable:
    new = 32 + ((b - 32 - shift) % 95)
    decoded += chr(new)

  start = 0
  while True:
    idx = decoded.find("CTFlearn{", start)
    if idx == -1:
      break
    end_idx = decoded.find("}", idx)
    if end_idx != -1:
      flag = decoded[idx:end_idx+1]
      print(f"Shift {shift}: {flag}")
    start = idx + 1
```
Running this program reveals the flag that appears on Shift 17.
