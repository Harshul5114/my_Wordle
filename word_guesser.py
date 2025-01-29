import json
import random

def load_words():
    with open(r'Wordle\words_dictionary.json') as word_file:

        word_dict = json.load(word_file)
        valid_words = set(word_dict.keys())
    return valid_words


class WordGuess:
    def __init__(self, word=None, randomize=False, length = 5):
        self.eng_dictionary = load_words()  # Load the dictionary of valid words
        
        if randomize:
            self.word = random.choice([w for w in self.eng_dictionary if len(w) == length]).upper()
        else:
            self.word = word.upper() if word else None

        print(self)
    
    def guess(self, guessWord = '') -> list:
        """returns a list of states"""
        if guessWord == '':
            raise Exception('no word guessed!')
        if len(guessWord) != len(self.word):
            raise Exception('invalid length')
        
        cor = False
        let_count = {} 
        valid = self.checkValidity(guessWord)
        
        res = ['grey']*len(self.word)
        for i in range(len(guessWord)):
            guess_letter = guessWord[i].upper()
            if guess_letter == self.word[i]:
                res[i] = 'green'
                let_count[guess_letter] = let_count.get(guess_letter,0) + 1

        for i in range(len(guessWord)):
            guess_letter = guessWord[i].upper()
            if (res[i] == 'grey' and
                guess_letter in self.word
                and let_count.get(guess_letter,0) < self.word.count(guess_letter)): 
                res[i] = 'yellow'
                let_count[guess_letter] = let_count.get(guess_letter,0) + 1
        
        if res.count('green') == len(res):
            cor = True


        return res, cor, valid
    
    def checkValidity(self, word):
        return (word.lower() in self.eng_dictionary)
    
    def __repr__(self):
        return f'Word: {self.word}'




        
