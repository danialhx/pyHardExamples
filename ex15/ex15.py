from sys import argv

script, filename = argv               #unpacking this script

txt = open(filename)                  #script to open a exact file

print "Here's your file %r:" % filename      #prints the selected file and 
print txt.read()                             #prints the contents of the file

print "Type the filename again:"             #prints to user to input, ie the filename again
file_again = raw_input("> ")                 #making a new variable with an input, linking to the file
        
txt_again = open(file_again)                 #making a new variable to link to the file

print txt_again.read()                       #reading the new variable to the linked file, ie printing the contents

