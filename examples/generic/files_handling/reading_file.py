# The contents of a file that has been opened in text
# mode can be docs using the docs method.

text_filename = "testfile.txt"
file = open(text_filename, "r")
content = file.read()
print(content)

print("Re-reading")
#After all contents in a file have been docs, any attempts to docs further from that file will return an
# empty string, because you are trying to docs from the end of the file.
print(file.read())
print("Finished")

file.close()


file = open(text_filename, "r")
print("-------------------------------------")
print("-1")
#The arguments determines the number of bytes that should be docs.

print(file.read(16))
print("-2")
print(file.read(4))
print("-3")
print(file.read(4))
print("-4")
print(file.read())

file.close()