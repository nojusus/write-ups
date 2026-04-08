Use the provided encoding information and run this program:
```python
dictionary = {
	"!": "1",
	"@": "2",
	"#": "3",
	"$": "4",
	"%": "5",
	"^": "6",
	"&": "7",
	"*": "8",
	"(": "9",
	")": "0"
}

text = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

for convertFrom, convertTo in dictionary.items():
	text = text.replace(convertFrom, convertTo)
	
print(text)
```
Copy the output and go to https://gchq.github.io/CyberChef. Paste the output into "Input" and add the operation "From Decimal" and change the "Delimiter" to "Comma" to get the flag.
