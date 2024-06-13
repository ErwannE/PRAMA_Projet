# Importations

import numpy as np # Pour les calculs mathématiques
import matplotlib.pyplot as plt # Pour les graphiques
import pandas as pd # Pour la manipulation de tableaux de données
#
# from spellchecker import SpellChecker # Pour vérifier que le dataset d'entraînement ne contient pas de fautes d'orthographe ni de noms propres
import time # Pour mesurer le temps d'exécution

def remove_accents(text):
    text = text.replace('à', 'a')
    text = text.replace('â', 'a')
    text = text.replace('é', 'e')
    text = text.replace('è', 'e')
    text = text.replace('ê', 'e')
    text = text.replace('î', 'i')
    text = text.replace('ô', 'o')
    text = text.replace('ù', 'u')
    text = text.replace('û', 'u')
    text = text.replace('ç', 'c')
    text = text.replace('À', 'A')
    text = text.replace('Â', 'A')
    text = text.replace('É', 'E')
    text = text.replace('È', 'E')
    text = text.replace('Ê', 'E')
    text = text.replace('Î', 'I')
    text = text.replace('Ô', 'O')
    text = text.replace('Ù', 'U')
    text = text.replace('Û', 'U')
    text = text.replace('Ç', 'C')
    return text

def remove_special_chars(text):
    text = text.replace('.', '')
    text = text.replace('!', ' ')
    text = text.replace('?', ' ')
    text = text.replace("' ", ' ')
    text = text.replace("'", ' ')
    text = text.replace('"', ' ')
    text = text.replace(',', '')
    text = text.replace(';', ' ')
    text = text.replace('(', '')
    text = text.replace(')','')
    text = text.replace(': ', ' ')
    text = text.replace(':', ' ')
    text = text.replace('«', '')
    text = text.replace('»', '')
    text = text.replace('-', '')
    text = text.replace('-', '')
    text = text.replace('–', '')
    text = text.replace('’', ' ')
    return text

def remove_double_spaces(text):
    text = text.replace('  ', ' ')
    text = text.replace('   ', ' ')
    return text

def remove_numbers(text):
    text = ''.join([i for i in text if not i.isdigit()])
    return text

def text_preparation(file_path, number_char, verbose=False):
    # Ouverture du fichier
    number_char = min(number_char, 304390477) 
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read(number_char)

    # Suppression des caractères inintéressants
    text = text.lower() # On met tout en minuscule - abandonné car on a besoin des majuscules pour identifier les noms propres.
    #text = remove_accents(text) # On enlève les accents
    text = remove_special_chars(text) # On remplace les caractères spéciaux par des espaces
    text = remove_numbers(text) # On enlève les chiffres

    ## Vérification de la bonne orthographe des mots
    """
        spell = SpellChecker(language='fr')
        words = text.split()
        misspelled = spell.unknown(words)
        list_misspelled = [word for word in misspelled if len(word) > 1]
        print(list_misspelled) if verbose else None

        percentage_misspelled = round(len(list_misspelled) / len(words) * 100,2)
        print(f"Percentage of misspelled words: {percentage_misspelled:.2f}%") if verbose else None
    
        # C'est triché...
    # On supprime les mots mal orthographiés et les noms propres - LIMITANTE TEMPORELLEMENT
    time_start = time.time()

    print(f'Nouvelle longueur du texte: {len(text.split())} mots') if verbose else None
    for word in words:
        if word in list_misspelled:
            text = text.replace(word, '')

    time_end = time.time()
    execution_time = round(time_end - time_start,2)
    """
    execution_time = 0
    print(f'Temps d\'exécution: {execution_time} s') if verbose else None

    text = remove_double_spaces(text) # On enlève les doubles espaces dus à la suppression des mots et des caractères spéciaux

    return text,execution_time

