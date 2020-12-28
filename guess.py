import random


def intro():
    print("Hello! Welcome to the guessing game. What is your name?")
    name = input()
    print('well ' + name, ' I am thinking of a number between 1-20 ')
    guess(name)


def guess(name):
    cpu = random.randint(1, 20)
    #print(cpu)
    for guessTaken in range(1,6):
        print("Take a guess")
        playerEntry = int(input())
        if playerEntry < cpu:
            print('your guess is too low')
            continue
        elif playerEntry > cpu:
            print('your guess is too high')

        elif playerEntry == cpu:
            break

    if playerEntry == cpu:
        print('good job', name, 'you have guessed my number in %d ' % guessTaken,'guesses')

    if playerEntry != cpu:
        print('No, the number I was thining of was %d' % cpu)


intro()
