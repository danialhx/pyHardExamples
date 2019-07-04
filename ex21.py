def add(a,b):                           #function1
        print "ADDING %d + %d" % (a,b)
        return a + b

def subtract(a,b):                      #function2
        print "SUBTRACTING %d - %d" % (a,b)
        return a - b

def multiply(a,b):                      #function3
        print "MULTIPLYING %d * %d" % (a,b)
        return a * b

def divide(a,b):                        #function4
        print "DIVIDING %d / %d" % (a,b)
        return a / b

print "Let's do some math with just functions!"
#menggedik, boleh je letak int. tapi dia guna function
age = add(30,5)                 
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height:%d, Weight: %d, IQ: %d" %(age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight, divide(iq,2))))
#inside out first.
print "That becomes: ", what, " Can you do it by hand?"
