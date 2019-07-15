from sys import exit

def fox():
        print 'That is not a fox, its a red panda'
        print 'The panda swipes the sandwich from your hand and you pet it on the head while it is eating'
        exit(0)

def creek():
        print 'The creek is about a 4 feet wide with a rotten branch for a bridge'
        print '(Choices: jump or cross the bridge?)'
        
        next = raw_input('> ')
        if next == "jump":
                print "The fox is moving nearer to you"
                fox()
        elif next == 'cross the bridge':
                dead('The bridge broke and stab you in the back')
        else:
                dead('The fox ran away')

def dead(why):
        print why, "Good job!"

def start():
        print 'You are in the woods eating your sandwich'
        print 'There is a fox, it saw you and ran under the bushes'
        print 'You looked under the bush, it is too thick and small'
        print 'Would you like to move around the bush or climb the dead tree branch above it? (Choices: around the bush, climb tree)'
        next = raw_input('> ')
        
        if next == 'around the bush':
                print 'There is a creek behind the bush'
                print 'The fox saw you, it jumped over the creek'
                creek()
        elif next == 'climb tree':
                dead('The branch broke off and fell on your head')
        else:
                dead('The fox ran away')
                

start()
