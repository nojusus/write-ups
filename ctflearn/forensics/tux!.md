Running the command
```bash
file Tux.jpg
```
reveals a comment containing an encoded base64 string. The string can be decoded using the command
```bash
echo "ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIzNDUK" | base64 -d
```
that reveals a password. Running the command
```bash
binwalk Tux.jpg
```
shows that the image contains hidden files that can be extracted using
```bash
binwalk -e Tux.jpg
```
and a new file "1570.zip" can be found. Extracting the file using
```bash
unzip 1570.zip
```
and entering the password that was found previously, the flag file can be found and read using
```bash
cat flag
```
