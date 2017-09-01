# opens user-defined file and write user-defined string to it

file_name = input("Enter file name: ")
file = open(file_name,"w")
file_contents = input("Enter string to write to file: ")
file.write(file_contents)
file.close()
