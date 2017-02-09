import random

print "I am thinking of a number between 1 and 10"

chances = 5;
win = random.randint(1, 10)


while chances > 0:

    entry = int(raw_input("What is your number?"))





    if entry == win:
        print ("A winner is you!")
        chances = 0
    elif (entry > 10 or entry < 0):
        print ("The number is between 1 and 10!")
    elif entry < win:
        print "%d is too low!" % entry
        chances -= 1
        print ("You have %s chances left") % chances
    elif entry > win:
        print "%d is too high!" % entry
        chances -=1
        print ("You have %s chances left") % chances;



    if chances == 0:
        again = raw_input("Try again? (yes/no)")
        if (again == 'yes'):
            chances = 5
            win = random.randint(1, 10)
