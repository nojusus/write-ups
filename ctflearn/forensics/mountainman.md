Examining the image with the command
```bash
xxd MountainMan.jpg
```
shows that there is hidden information inside the bottom bytes, since FF D9 bytes should be the end of an jpg file. Copying these bytes over to CyberChef and using the Magic tool with the intensive mode, the flag can be found decoded from hex.
