Checking the image for hidden files using
```bash
binwalk oreo.jpg
```
reveals that there are files to be extracted. Extracting with
```bash
binwalk -e oreo.jpg
```
provides a second image that has the flag that can be found by running
```bash
strings b.jpg
```
and scrolling to the bottom of the output.
