Download the provided file "Begin Hack.jpg" and run the command
```bash
strings "Begin Hack.jpg" | grep mega
```
to get a download link for another file. Extract the file, enter the folder's directory and run the command
```bash
ls -la
```
to find a hidden file ".Processing.cerb4". Run the command
```bash
binwalk -e .Processing.cerb4
```
to get a locked file "0.zip". Go back to the first file and run the command
```bash
strings "Begin Hack.jpg" | grep key
```
Use the found string as the password to extract the file. Open the extracted file "skycoder.jpg" and look at the bottom right corner to get the flag.
