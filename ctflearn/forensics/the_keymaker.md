Running the command
```bash
file The-Keymaker.jpg
```
shows 3 comments that contain a fake flag, a base64 encoded string, and a aes-256-cbc encoded string. Decoding the base64 string using
```bash
echo "b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg" | base64 -d
```
reveals the neccessary command to decode the final string, with 2 still being missing. Using jpdump for the image, the SOF0 and SOS keys can be found as marker IDs. Going to HexEd with the image, to obtain the first key needed for the initialization vector, search for the marker ID bytes, skip 2 bytes after it, copy the next 16 bytes and turn them into a hex string, that is the first key. Do the same for the second key by locating the other marker ID bytes, but this time don't skip 2 bytes, just copy 32 bytes after the marker ID, and turn them into a hex string. That is the second key. Finally, create a new file called "flag.enc" and paste the aes-256-cbc encoded string that was found in the beginning inside of it. Run the final command with your obtained keys and export the output with
```bash
openssl enc -d -aes-256-cbc -iv 0800be00c803011100021101031101ff -K 000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952 -in flag.enc -out flag -base64
```
to obtain the flag.
