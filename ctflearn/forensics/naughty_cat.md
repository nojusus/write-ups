Running the command
```bash
binwalk cut3_c4t.png
```
shows that there are hidden files inside the image. Running the command
```bash
binwalk -e cut3_c4t.png
```
extracts them. The only ones you're gonna need are "purrr_2.mp3" and "y0u_4r3_cl0s3.rar". Start by opening the mp3 file with Audacity using
```bash
audacity purrr_2.mp3
```
Once you're in Audacity, click on the three dots properties icon next to the file's name and click Spectrogram. If you extend the audio track down, you obtain a string that is going to be used as a password. Next, trying to extract the rar file will not work since it's header is broken. HexEd is a good tool for this purpose, so open the rar file and change the first 4 bytes to 52 61 72 21 to have a header "Rar!" instead of "Cat!". Save the fixed rar file, and extract it using
```bash
unrar x fixed.rar
```
The extraction will require the password you obtain from the mp3 file's spectrogram. A file "f1n4lly.txt" is extracted that contains an encoded string that can be decoded using
```bash
echo "ZjByM241MWNzX21hNXQzcg==" | base64 -d
```
to produce the flag.
