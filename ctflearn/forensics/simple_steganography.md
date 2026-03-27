Running the command
```bash
strings Minions1.jpeg
```
and scrolling to the top of the output, a password "myadmin" can be found. Using the command
```bash
steghide extract -sf Minions1.jpeg
```
and typing in the found password, a file "raw.txt" is extracted, containing a string that is encoded with base64. The string is decodable with
```bash
echo "AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9" | base64 -d
```
and the flag gets revealed.
