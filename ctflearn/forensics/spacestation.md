Running the command
```bash
binwalk SpaceStation.jpg
```
shows that there are hidden files that can be extracted using
```bash
binwalk -e SpaceStation.jpg
```
The extracted "readme" file provides complete instructions to obtaining the flag. The flag is inside the "flag.enc" file which requires the initialization vector and a key. Following the instructions, the vector can be obtained by running
```bash
objdump -d -j .data Bangalore
```
and scrolling up to the "welcome" header to copy the first 16 bytes, ignoring all 00 bytes. The key is acquired the same way by running
```bash
objdump -d -j .text Bangalore
```
and scroling up to the "_flagLoop" header to copy the first 32 bytes, ignoring all 00 bytes. Finally, combining the acquired strings into the final command
```bash
openssl -enc -d -aes-256-cbc -iv 48656c6c6f204354466c6561726e2042 -K 4889cfe83de849e858e86688875c2540c6875d25400ac687e254048b85c2540 -in flag.enc -out flag.txt
```
produces the flag.
