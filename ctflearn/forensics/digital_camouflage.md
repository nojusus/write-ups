Opening the "data.pcap" file in Wireshark and searching for "http.request.method", a POST method can be found and traced along with Right Click > Follow > TCP Stream and locating the password. The password is under a base64 encoding, that also contains a wrong tail. Firstly, change the tail from "%3D%3D" to "==" to get a decodable string, then decode the string with
```bash
echo "UEFwZHNqUlRhZQ==" | base64 -d
```
to produce a string, that you can wrap inside the most common prefix to produce the actual flag.
