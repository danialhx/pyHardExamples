def whileLoops():
        i = 0
        numbers = []

        for i in range(0,7):
                print "At the top i is %d" % i
                numbers.append(i)

                print "Numbers now: ", numbers
                print "Aat the bottom i is %d" % i 

        print "The numbers: "

        for num in numbers:
                print num

whileLoops()
