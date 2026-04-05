Download the provided file "The-Keymaker.jpg" and run the command
```bash
file The-Keymaker.jpg
```
There are 3 hidden comments. Remember the third string. Decode the second string with the command
```bash
echo YourStringHere | base64 -d
```
Go to https://cyber.meme.tips/jpdump and select the image. Find the SOF0 and SOS markers. Go to https://hexed.it. Search for the SOF0 bytes, skip 2 bytes after it and copy the next 16 bytes, turn them into a string and save it. Do the same for the SOS marker, but don't skip 2 bytes. Copy 32 bytes after the marker, turn them into a string and save it. Create a new file "flag.enc" and paste the third string from the first command into it. Run the final command
```bash
openssl enc -d -aes-256-cbc -iv YourFirstString -K YourSecondString -in flag.enc -out flag -base64
```
to get the flag.
