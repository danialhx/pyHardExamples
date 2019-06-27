from sys import argv

script, filename = argv

txt = open(filename)

print "reading following file %r:" % filename
print txt.read()

