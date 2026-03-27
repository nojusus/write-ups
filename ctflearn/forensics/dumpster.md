Extract the downloaded zip file using
```bash
unzip dumpster.zip
```
The Decryptor.java file reveals that the flag is encrypted and requires a hash password to decrypt it. VisualVM is a good tool to dig through the heapdump.hprof file. Open it with
```bash
visualvm
```
Go to File > Load > Find your heapdump.hprof file and select it. Change the view from Summary to Threads and scroll to the bottom to find the Decryptor.main thread. Continue going down in Decryptor.main > Decryptor$Password#1 > fields > passHash. Keep VisualVM open and go back to the Decryptor.java program. Modify it to this version:
```java
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Decryptor
{
  public static final String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";
  public static byte[] decrypt(byte[] msg, byte [] passHash) throws Exception
  {
    SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
    Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
    Cipher.init(Cipher.DECRYPT_MODE, spec);
    return cipher.doFinal(msg);
  }
  public static void main(String[] args) throws Exception
  {
    byte[] passHash = {};
    System.out.println(new String(decrypt(Base64.getDecoder().decode(FLAG.getBytes()),passHash)));
  }
}
```
Inside the passHash array, write down the 16 acquired bytes from VisualVM, separating them with commas. Running the program with
```bash
java Decryptor.java
```
reveals the flag.
