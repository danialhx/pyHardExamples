from sys import argv

script, input_file = argv

def print_all(f):    #function to read file
        print f.read()  #prints and reads the file

def rewind(f):                  #function to restart the file. 
        f.seek(0)               #moves read head back to zeroth byte

def print_a_line(line_count, f):        #function arg1=current line, arg2 = current file.  
        print line_count, f.readline()  #will display line, and will read only the line

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1        #initialise current_line variable
print_a_line(current_line, current_file)

current_line = current_line + 1        #incrementing current line
print_a_line(current_line, current_file)

current_line = current_line + 1 #2nd increment. 
print_a_line(current_line, current_file)

