import random

def gameControl():
    num = random.randint(0, 4)
    print "Howdy, what's your name?"
    name = raw_input('')
    print name + ", I'm thinking of a number between 1 and 100. Try to guess my number."
    evaluate(num, name)

def evaluate(num, name):
    playAgain = True
    while playAgain == True:
        guess = -1
        count = 0
        while(guess != num)     :
            tuple = validate(guess, num, count)
            guess = tuple[0]
            count = tuple[1]
        print 'Well done, ' + name + '! You found my number in ' + str(count) + ' tries!'
        print "Wanna play again?"
        pa = raw_input('...?')
        if pa.upper() not in "YES Y":
            playAgain = False

def validate(guess, num, count):
    try: 
        print 'Your guess? '
        guess = int(raw_input(''))
        if guess < num and guess > 0:
            print "pick a higher number"
        elif guess > num and guess < 100:
            print "pick a lower number"   
        elif guess < 0 or guess > 100:
            print "That number is way out of range of 1 to 100!" 
        count += 1 
        print str(count) + 'count validate'
        print str(guess) + 'guess validate'
        return (guess, count)
    except ValueError:
        print "Please enter a valid integer"


gameControl()