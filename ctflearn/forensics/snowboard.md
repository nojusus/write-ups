Running the command
```bash
file Snowboard.jpg
```
reveals 2 comments, that contain a fake flag and a string that is encoded with base64. The string can be decoded with the command
```bash
echo "Q1RGbGVhcm57U2tpQmFuZmZ9Cg==" | base64 -d
```
that reveals the real flag.
