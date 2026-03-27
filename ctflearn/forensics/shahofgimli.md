Running the command
```bash
binwalk ShahOfGimli.jpg
```
shows that there are hidden files inside the image that can be extracted using
```bash
binwalk -e ShahOfGimli.jpg
```
Extracting the obtained "20517" Tar file, 2 new files "flag.enc" and "Gimli04Base.jpg" are obtained. Running the command
```bash
strings ShahOfGimli.jpg
```
and scrolling to the top of the output to decode the first base64 string, a clue can be found that SHA-256 was used. Running the command
```bash
sha256sum Gimli04Base.jpg
```
gives a key that must be used in the final command, which is
```bash
openssl enc -d -aes-256-cbc -iv 00000000000000000000000000000000 -K e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87 -in flag.enc -out flag.txt
```
which reveals the flag.
