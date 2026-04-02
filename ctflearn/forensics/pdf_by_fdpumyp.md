Download the provided file "dontopen.pdf" and run the command
```bash
strings dontopen.pdf | grep external
```
to get an encoded string. Decode it with the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
