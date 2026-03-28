Running the command
```bash
exiftool bobbytoesipad.png
```
reveals a warning that there is trailer data after the IEND chunk. Open the file inside HexEd and locate the bytes 49 45 4E 44, which is the IEND marker. Skip another 4 bytes after them, and an FF D8 marker can be found, which suggests a hidden JPG file. The file turns out to be broken containing a wrong length byte and extra stuffed data. Locate the length byte 2 bytes to the right from FF E0. Change it from 63 to 10. Next, select 39 bytes after the length byte and Right Click > Delete selected bytes. Export the fixed trailer bytes from FF D8 to FF D9 as a JPG file. The new image contains a string that will be used later. Open Stegsolve using
```bash
java -jar Stegsolve.jar
```
Open the bobbytoesipad.png file and try different color maps until you find another hidden string. Go into CyberChef and choose Vigenère Decode. In the Input, type in the string from the bobbytoesipad.png file, and in the Key, type in the string from the fixed JPG file. The Output should produce a readable string, that should be wrapped under the most common flag prefix and work as the flag.
