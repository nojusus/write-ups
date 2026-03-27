Running the command
```bash
wireshark 'flag (4)'
```
will launch Wireshark where the packet can be analyzed. In the search field, filtering for "http.request.method" provides all HTTP frames, since they are most likely to contain information. The frame 247 contains an encoded message that can be decoded using
```bash
echo "ZmxhZ3tBRmxhZ0luUENBUH0=" | base64 -d
```
to produce the flag.
