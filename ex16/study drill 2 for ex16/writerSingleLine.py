from sys import argv

script, filename = argv

print "File will be opened in write mode"
target = open(filename, 'w')

lines = ("Mary had a little lamb", "It's fleece was white as snow", "It was also tasty")

target.write("\n".join(lines)) #seperator \n, nextline and .join(string)
target.close()
print "%r closed" %filename


