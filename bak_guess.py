import random

def gameControl():
    
    num = random.randint(1, 100)
    print num

    print "Howdy, what's your name?"
    name = raw_input('')
    print name + ", I'm thinking of a number between 1 and 100. Try to guess my number."

    evaluate(num, name)




def evaluate(num, name):

    playAgain = True

    while playAgain == True:
        
        guess = -1
        count = 0
        bestScore = 100000

        while(guess != num):

            print 'Your guess? '
            guess = int(raw_input(''))

            try: 
                game_results = round_check(guess, num, count) 
            except ValueError:
                print 'Please enter a valid integer.'

            guess = game_results[0]
            count = game_results[1]    

        print 'Well done, ' + name + '! You found my number in ' + str(count) + ' tries!'
        if count < bestScore:
            bestScore = count
        print "Your current best score is: " + str(bestScore)
        print "Wanna play again?"
        
        pa = raw_input('...?')
        if pa.upper() not in "YES Y":
            playAgain = False
            print "bye!"




def round_check(guess, num, count):
        if guess < 1 or guess > 100:
            print "That number is way out of range of 1 to 100!"
        elif guess < num:
            print "pick a higher number"
        elif guess > num:
            print "pick a lower number"   
        else:
            print "win!"

        count += 1 
        return (guess, count)
        




gameControl()




