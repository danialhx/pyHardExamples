def cheese_and_crackers(cheese_count, boxes_of_crackers):
#defining the function
        print "You have %d cheeses!" % cheese_count
        print "You have %d boxes of crackers!" % boxes_of_crackers
        print "Man that's enough for a party!"
        print "Get a blanket. \n"

#defining different arguments for the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"   
#adjusting the argv in the function
amount_of_cheese = 10
amount_of_crackers = 50

#new def with new args
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#args not used, but utilise numbers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#using args and some numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
