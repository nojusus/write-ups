Running the command
```bash
file Gandalf.jpg
```
reveals 3 comments, that each contain a base64 encoded string. The first one is decodable with
```bash
echo "Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=" | base64 -d
```
and it reveals a fake flag that is meant to be used as a hint for the other two. The solution requires XOR use, so a Python program is a good solution.
```python
import base64

a = "xD6kfO2UrE5SnLQ6WgESK4kvd/Y/rDJPXNU45k/p"
A = base64.b64decode(a)
b = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"
B = base64.b64decode(b)
c = []
l = len(A)

for i in range(l):
  c.append(chr(A[i] ^ B[i]))

print("".join(c))
```
Running this program prints out the flag.
