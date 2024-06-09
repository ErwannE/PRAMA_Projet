#J'utilise ce document pour créer de nouveau corpus, l'original étai trop long pour être utilisé dans le code.
file_path = 'c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/toy_corpus/europarl-v6.fr-en.fr_real_new.txt' 

try:
    file = open(file_path, 'r', encoding='utf-8')
except IOError:
    print("Erreur lors de l'ouverture du fichier.")
text = file.read()

n = 5000000
new_file_path = f'c:/Users/erwan/Documents/ENPC/2A/PRAMA/PRAMA_Projet/toy_corpus/new_corpus_{n}_fixed.txt'

try:
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(text[:n])
except IOError:
    print("Erreur lors de la création du nouveau fichier.")


print(f'New corpus created at {new_file_path}')