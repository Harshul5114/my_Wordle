import word_guesser
heh = word_guesser.WordGuess('SQUID')
chance = 0
col_map = {'green': '🟩', 'yellow': '🟨', 'grey':'⬜'}
while chance < 5:
    try:
        word = input("enter guess: ")
        res = heh.guess(word)[0]
        hmm = map(lambda x: col_map[x], res)
        print(*hmm)
        print(' ', end = '')
        print('  '.join(list(word)))
    except Exception as e:
        print(f'**{e}**')
        print('Try again!')
    
