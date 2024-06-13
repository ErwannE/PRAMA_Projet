import random
from math import ceil, inf
import copy
from collections import defaultdict
from math import log10

def read_file(file_path):
    # Ouvrir le fichier en mode lecture
    with open(file_path, 'r', encoding='utf-8') as file:
        # Lire toutes les lignes dans le fichier
        lines = file.readlines()

    # Créer une liste pour stocker toutes les phrases
    sentences = []

    # Pour chaque ligne dans le fichier
    for line in lines:
        # Supprimer les espaces de début et de fin
        line = line.strip()
        # Séparer la ligne en mots en utilisant l'espace comme séparateur
        words = line.split(' ')
        # Ajouter les mots à la liste des phrases
        sentences.append(words)

    # Maintenant, 'sentences' est une liste de listes, où chaque sous-liste est une phrase du document, divisée en mots.
    return sentences

# L'implementaiton de cette classe est tirée d'un document de DHRUV DESHMUKH
# General class for n-gram
class N_gram:
    def __init__(self, n=1):
        self.n = n
        self.prob_dict = {}
        self.min_prob = 1.0 #used when we get 0 prob
        self.dictionary = defaultdict(int)
        self.longest_word_length = 0
        self.cnt = 0

    # Function to train the model using a given corpus
    def train(self, corpus):
        count_n = {}
        count_n_1 = {}

        for sentence in corpus:
            cur_context = ''
            for i in range(len(sentence)):
                if(cur_context in count_n_1):
                    count_n_1[cur_context]+=1
                else: 
                    count_n_1[cur_context]=1
                if((sentence[i], cur_context) in count_n):
                    count_n[(sentence[i],cur_context)]+=1
                else: 
                    count_n[(sentence[i],cur_context)]=1
                # print((corpus[i],cur_context))
                self.dictionary[sentence[i]]+=1
                self.cnt+=1
                self.longest_word_length = max(self.longest_word_length, len(sentence[i]))
                # if(sentence[i] in ['t','h','e','f']): print(sentence[i], sentence)
                cur_context+=sentence[i]
                if i >= self.n-1:
                    removeLen = len(sentence[i-self.n+1])
                    cur_context = cur_context[removeLen:]

        for key in count_n.keys():
            if key[1] not in self.prob_dict:
                self.prob_dict[key[1]] = dict()
            self.prob_dict[key[1]][key[0]] = round(count_n[key]/count_n_1[key[1]],3)
            if self.prob_dict[key[1]][key[0]] == 0.0:
                self.prob_dict[key[1]][key[0]] = 0.0001
            # if(self.prob_dict[key[1]][key[0]] == 0):
            #     print(count_n[key],count_n_1[key[1]])
            self.min_prob = min(self.min_prob, self.prob_dict[key[1]][key[0]])
        # print(self.min_prob)
        self.min_prob = log10(self.min_prob)
        
        # print("i:",count_n[("","of")])
        # print(count_n_1["i"])
        # print(self.prob_dict)


    # Get the probablility of a word occuring given a certain context
    def get_prob(self, context, cur_word):
        if context not in self.prob_dict or cur_word not in self.prob_dict[context]:
            # print("in:",cur_word)
            return 0.001*log10(self.dictionary[cur_word] + 1)
        # print(self.prob_dict[context][cur_word])
        return log10(self.prob_dict[context][cur_word]/0.001)


"""
import pickle

# Créer une instance de N_gram
three_gram = N_gram(3)
sentences = read_file('c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/toy_corpus/cleaned_text_100000000.txt')
three_gram.train(sentences)

# Sauvegarder l'instance dans un fichier
with open('c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/three_gram_100000000.pkl', 'wb') as f:
    pickle.dump(three_gram, f)

print("OK")

with open('c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/three_gram_100000000.pkl', 'rb') as f:
    loaded_three_gram = pickle.load(f)

print("loaeded successfully")

print(loaded_three_gram.get_s_prob('le', 'jrjgj'))
print(loaded_three_gram.get_s_prob('le', "gang"))
print(loaded_three_gram.get_s_prob('le', 'parlement'))
"""
      