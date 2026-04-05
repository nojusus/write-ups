Download the provided file "unopenable.gif" and go to https://hexed.it. Open the file, select the first byte, right click, select "Insert Bytes Here..." and insert 4 new bytes. Type in 47 49 46 38, save the new file and open it to find an encoded string. Decode it with the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
