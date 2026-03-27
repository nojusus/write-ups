Once the zip file is extracted, a file "The Flag.pdf" can be found that that requires a password. Running the command
```bash
ls -la
```
shows a hidden directory .ThePassword. The directory can be accessed with
```bash
cd .ThePassword
```
Running the first command again, a hidden file "ThePassword.txt" can be found that can be read with
```bash
cat ThePassword.txt
```
that reveals a password that is used for the pdf file, which reveals the flag.
