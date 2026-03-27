Running the command
```bash
strings dontopen.pdf
```
and looking at the bottom of the output, an encoded base64 string can be found and decoded using
```bash
echo "Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==" | base64 -d
```
that reveals the flag.
