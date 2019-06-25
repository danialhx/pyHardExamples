from sys import argv

script, filename = argv                               #start with on terminal, python ex16.py test.txt

print "We're going to erase %r." %filename              #test.txt is %filename
print "If you don't want that, hit CTRL-C (^C)."        #doesn't do anything except breaks the script
print "If you do want that. hit RETURN."                #script continues

raw_input("?")                                          #press enter and all in test.txt will be erased

print "Opening the file..."
target = open(filename,'w')                             #opens test.txt

print "Truncating the file. Goodbye!"
target.truncate()                                       #reduces the size of the file, but ()empty erases the test.txt to empty

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")                           #creates variable line1 with raw input from terminal
line2 = raw_input("line 2: ")                           #var line2
line3 = raw_input("line 3: ")                           #var line3

print "I'm going to write these to the file."

target.write(line1)                                    #will take variable = line1 target.write(var), starts from line 1
target.write("\n")                                     #jumps to next line
target.write(line2)                          #writes var line2 to the line(now line 2)                                                         
target.write("\n")                           #jumps to next line
target.write(line3)                          #writes var line3 to current line(now line 3
target.write("\n")                             

print "And finally, we close it."
target.close()                                  #closes test.txt
