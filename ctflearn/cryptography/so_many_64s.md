Download the provided file "flag.txt" and run this program:
```python
import base64

with open("flag.txt", "rb") as f:
	last_string = f.read()
	while b"CTF{" not in last_string:
		last_string = base64.b64decode(last_string)
	print(last_string)
```
to get the flag.
