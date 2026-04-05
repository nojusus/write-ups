Download the provided file "dumpster.zip", extract it and run the command
```bash
visualvm
```
Go to "File" > "Load" > "heapdump.hprof". Change the view from "Summary" to "Threads". Scroll to the bottom and find the "Decryptor.main" thread. Go down to "Decryptor$Password#1" > "fields" > "passHash". Go back to the "Decryptor.java" program and modify it to this version:
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
Inside the "passHash" array, type in the 16 bytes from "passHash" in VirtualVM, separating them with commas. Run the command
```bash
java Decryptor.java
```
to get the flag.
