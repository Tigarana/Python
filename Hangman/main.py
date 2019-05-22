import time
import getpass
import targetWord
import hangmanDrawer

'This will simulate the HangMan game.'
'One player sets up a word. The other one needs to try and guess the word'


print('Welcome to this breath-taking game of Hangman.')
time.sleep(2)
print('If you play with two people, you can choose a word for the other person to guess. ')
time.sleep(2)
print('If you play alone, a random word will be chosen for you. \n')
time.sleep(2)

# define number of players
alone = ''
while alone != 'y' and alone != 'n':
    print('Are you playing alone?')
    alone = input(
        'Please answer \'y\' if you are playing alone and \'n\' if you are playing with two? ')

# Create targetWord
if alone == 'y':
    target = targetWord.targetWord()
else:
    print()
    print('Player 1: ')
    time.sleep(2)
    tmp = getpass.getpass('Please enter your secret word now. ')
    target = targetWord.targetWord(tmp)

hangman = hangmanDrawer.hangmanDrawer()

print()
print('Hangman: ')
time.sleep(2)
print('Let\'s get started. ')
time.sleep(1)
print('You can type in a letter or make a guess for the complete word. ')
print('If the letter is not present in the word, or if you make a wrong guess, you have a failed attempt. \n')
time.sleep(2)
print('The word that you are looking for has %d letters. ' % len(target.target))
time.sleep(1)
print('You have %d attempts to find this word... Or you\'ll hang. ' %
      hangman.maxTries)
time.sleep(3)

won  = False
lost = False
while not won and not lost:
    print()
    print('Attempts: ', end='', flush=True)
    hangman.drawHangman()
    print()
    print('Mystery word: ', end='', flush=True)
    target.displayWord()
    print()
    succes = ''
    while succes == '':    
        time.sleep(1)    
        guess = input('Make your best guess: ')
        succes = target.check(guess)
    if succes:
        won = target.gameWon()
    else:
        hangman.failedAttemt()
        lost = (hangman.failedTries == hangman.maxTries)
    time.sleep(2)

if lost:
    print()
    print('The correct word was \'%s\'.' % target.target)
    print()
    time.sleep(2)
    hangman.drawHangman()
# else won

