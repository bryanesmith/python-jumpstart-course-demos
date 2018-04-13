import random

print('--------------------------------------------------------')
print('                  GUESS THAT NUMBER')
print('--------------------------------------------------------')
print

number = random.randint(0, 100)
guess = -1

while guess != number:
    try:
        guess = int(input('Guess a number between 0 and 100: '))

        if guess < number:
            print('Your guess of {0} is too low...'.format(guess))
        elif guess > number:
            print('Your guess of {0} is too high...'.format(guess))
        else:
            print "You win!"

    except Exception as e:
        print('An error happened, try again...')

