from ngram import *
from data_preparation_function import *
import pickle
print("loading ngram...")
# PARAMETER
taille_ngram = 3
path_corpus = 'c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/toy_corpus\cleaned_text_10000000.txt'
with open('c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/three_gram.pkl', 'rb') as f:
    loaded_three_gram = pickle.load(f)
    print("ngram loaded")
class Guess:
    """To use main, just give a sentence (in Guess constructor) and use "correct" method it will correct the last word"""
    def __init__(self, text):
        text = text.lower() # On met tout en minuscule - abandonné car on a besoin des majuscules pour identifier les noms propres.
         #text = remove_accents(text) # On enlève les accents
        text = remove_special_chars(text) # On remplace les caractères spéciaux par des espaces
        text = remove_numbers(text) # On enlève les chiffres
        words = text.split()
        self.size = len(words)
        self.last_word = words[-1]
        self.context = ''.join(words[-taille_ngram:-1])

    def correct(self):
        prob = -1000
        best_word = self.last_word
        for word in loaded_three_gram.dictionary.keys():
            prob_temp = loaded_three_gram.get_prob(self.context, word)
            if prob_temp > prob:
                print(f"word: {word}, prob: {prob_temp}")
                prob = prob_temp
                best_word = word
        return best_word

def guess_sentence(text):
    for i in range(3, len(text.split())):
        sentence = " ".join(text.split()[:i])
        print(f"Sentence: {sentence}")
        guess = Guess(sentence)
        print(f"Context: {guess.context}")
        print(guess.correct())

guess_sentence("Il est très important de faire attention à la qualité de l'air que nous respirons.")


