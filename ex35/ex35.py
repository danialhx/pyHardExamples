from sys import exit

def gold_room():
        print "This room is full of gold. How much do you take?"

        next = raw_input("> ")
               
        if "0" in next or "1" in next: #takes input 0,1,10 and above 
                how_much = int(next)         
        else: #bug, 2-9 doesn't work
                dead("Man, learn to type a number.")

        if how_much < 50: #makes numbers above nine to be inputted
                print "Nice, you're not greedy, you win!"       
                exit(0)
        else:
                dead("You greedy bastard!")

def bear_room():
        print "There is a bear here."
        print "The bear has a bunch of honey."
        print "The fat bear is in front of another door."
        print 
        bear_moved = False

        while True:
                print("Choices: take honey, taunt bear(FirstChoice)")
                next = raw_input("> ")
                

                if next == "take honey":
                        dead("The bear looks at you then slaps your face off.")
                elif next == "taunt bear" and not bear_moved:
                        print "The bear has moved from the door. You can go through it now."
                        bear_moved = True
                        print("Choices: taunt bear, open door(SecondChoice)")
                elif next == "taunt bear" and bear_moved:
                        dead("The bear gets pissed off and chews your leg off.")
                elif next == "open door" and bear_moved:
                        gold_room()
                else:
                        print  "I got no idea what that means."

def cthulhu_room():
        print "Here you see the great evil Cthulhu."
        print "He, it, whatever stares at you and you go insane."
        print "Do you flee for your life or eat your head?"

        next =  raw_inlut("> ")

        if "flee" in next:
                start
        elif "head" in next:
                dead("Well that was tasty!")
        else: 
                cthulhu_room()

def dead(why):
        print why, "Good job!"
        exit(0)

def start():
        print "Your are in a dark room."
        print "There is a door to your right and left."
        print "Which one do you take?"


        print ("Choices : left,right,anything else")
        next = raw_input("> ")
        
        if next == "left":
                bear_room()
        elif next == "right":
                cthulhu_room()
        else:
                dead("You stumble around the room until you starve.")

start()
