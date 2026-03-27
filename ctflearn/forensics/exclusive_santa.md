Extract the downloaded rar file using
```bash
binwalk -e Exclusive_Santa.rar
```
The files you're gonna need are "1.png" and "3.png". The challenge already provides a hint that XOR is necessary as well as the file "3.png" suggests that you need to merge 2 different images. Running the command
```bash
binwalk 3.png
```
shows that there is a hidden png inside the file. Extract it using
```bash
foremost -i 3.png
```
You will find a new image file "00000102.png". Go into Stegsolve using
```bash
java -jar Stegsolve.jar
```
Open the file "1.png", go to Analyse > Image Combiner and select the "00000102.png" file. That should reveal the flag, but it's still hard to read it. Save the new image and mirror it horizontally with the command
```bash
convert solved.bmp -flop output.png
```
to be able to read the flag.
