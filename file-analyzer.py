# Program returns the number of times a user-specified character 
# appears in a user-specified file

def char_count(text, char):
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count

filename = input("Enter file name: ")
charname = input ("Enter character to analyze: ")

with open(filename) as f:
	data = f.read()

print (char_count(data, charname))
