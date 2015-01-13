import random

def loop():
    num = random.randint(0, 100)
    print "Howdy, what's your name?"
    name = raw_input('')
    print name + ", I'm thinking of a number between 1 and 100. Try to guess my number."
    guess = -1
    count = 1
    while(guess != num):
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
        except ValueError:
            print "Please enter a valid integer"
        
    print 'Well done, ' + name + '! You found my number in ' + str(count) + ' tries!'

loop()