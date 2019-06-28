from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one lone too, how?
in_file = open(from_file)       #item1 in argv, original
indata = in_file.read()         #read item1            
out_file = open(to_file, 'w')         #item2 in argv, copy
out_file.write(indata)      #after opening file, this line copies item1 to item2

print "Alright, all done."

out_file.close()
in_file.close()         #closing both files

