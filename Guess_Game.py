secret_word = 'MISHU'
guess = ''
i = 0
guess_limit = 5
while i < 5:
    guess = input("Enter a word : ")
    guess = guess.upper()
    if guess == secret_word:
        break
    i += 1

if i < 5:
    print('**BINGO!** \nYou got the secret')
else:
    print('Hard Luck !!')