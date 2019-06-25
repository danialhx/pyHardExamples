from sys import argv

script, filename = argv                               #start with on terminal, python ex16.py test.txt

print "We're going to erase %r." %filename              #test.txt is %filename
print "If you don't want that, hit CTRL-C (^C)."        #doesn't do anything except breaks the script
print "If you do want that. hit RETURN."                #script continues

raw_input("?")                                          #press enter and all in test.txt will be erased

print "Opening the file..."
target = open(filename,'w')                             #opens test.txt

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")                           
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
