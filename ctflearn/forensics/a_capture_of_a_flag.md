Download the provided file "flag (4)" and run the command
```bash
wireshark "flag (4)"
```
Search for a filter "http" and find the frame 247. Copy the found encoded message and run the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
