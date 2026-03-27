Running the command
```bash
binwalk Hey_You.png
```
shows that there are files hidden inside the image. They can be extracted using
```bash
binwalk -e Hey_You.png
```
Entering inside the extracted folder's directory and running
```bash
ls -la
```
a hidden txt file can be found and read with
```bash
cat "..txt"
```
The file contains a download link for another image. The action is the same, using binwalk to extract the hidden files inside the second image. The extracted folder contains a third image and running the command
```bash
strings YouWon(Almost).jpg
```
and looking at the output from the top, we can find the flag's prefix, but the flag itself is still encoded in base64. Decode the string using
```bash
echo "VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=" | base64 -d
```
Keep decoding the obtained string repeatedly until a readable message appears and then wrap the message inside the previously found prefix.
