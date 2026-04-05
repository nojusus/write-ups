Download the provided file "SpaceStation.jpg" and run the command
```bash
binwalk -e SpaceStation.jpg
```
to extract hidden files. Run the command
```bash
objdump -d -j .data Bangalore | grep -A 3 welcome
```
Copy the first 16 bytes and save the string. Run the command
```bash
objdump -d -j .text Bangalore | grep -A 15 0401018
```
Copy the first 32 bytes ignoring all 00 bytes and save the string. Run the command
```bash
openssl -enc -d -aes-256-cbc -iv YourFirstString -K YourSecondString -in flag.enc -out flag.txt
```
to get the flag
