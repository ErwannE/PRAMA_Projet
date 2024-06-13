def is_len_words_near(mot_tapé, mot_dico):
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    n1 = len(mot_tapé)
    n2 = len(mot_dico)
    return ((n2-2 <= n1) & (n1 <= n2+2))

def score_len(mot_tapé, mot_dico, pénalité_max=2):
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    n1 = len(mot_tapé)
    n2 = len(mot_dico)
    score = 0
    if not is_len_words_near(mot_tapé, mot_dico):
        score = 1000
    elif ((n1 == n2-1) | (n1 == n2+1)):
        score += pénalité_max/2
    elif ((n1 == n2-2) | (n1 == n2+2)):
        score += pénalité_max
    return score

def is_first_letter_the_same(mot_tapé, mot_dico):
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    return (mot_tapé[0] == mot_dico[0])

def score_prem_lettre(mot_tapé, mot_dico):
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    if not is_first_letter_the_same(mot_tapé, mot_dico):
        score = 1000
        return score
    else:
        return 0
    
dict_proches_clavier = {"a":["&","é","z","s","q"],"z":["&","é","a","s","q","d","e","\""],"e":["\'","\"","z","s","f","d","r"],
    "t":["-","y","g","f","h","r","("],"y":["-","t","g","j","h","u","è"],"u":["_","y","k","j","h","i","è"],
    "i":["_","u","k","j","l","o","ç"],"o":["à","i","k","m","l","p","ç"],"p":["o","l","m","ù",")","à"],
    "q":["a","z","s","w","x","<"],"s":["a","z","k","q","d","w","x"],"d":["s","z","e","r","f","x","c"],
    "f":["e","r","t","d","g","c","v"],"g":["r","t","y","h","f","v","b"],"h":["t","y","u","g","j","b","n"],
    "j":["u","i","y","h","k","n",","],"k":["u","i","o","j","l",",",";"],"l":["i","o","p","k","m",";",":"],
    "m":["o","p","ù","l",":","!"],"w":["<","q","s","d","x"],"x":["q","s","d","c","w"],"c":["s","d","f","x","v"],
    "v":["f","g","c","b"],"b":["v","g","h","n"],"i":["b","h","j",","],"r":["\'","t","g","f","d","e","("],
    "n":["b","h","j"]}

#création d'un mapping pour vérifier si il y a faute d'accent
mapping_accent_to_lettre = {"é":"e", "è":"e", "ç":"c", "à":"a", "ù":"u", 'â':'a', 'ê':'e', 'î':'i', 'ô':'o', 'û':'u'}
list_accents = ['é', "è","ç","à","ù",'â','ê','î','ô', 'û']

def score_letter_diff(lettre_tapée, lettre_dico, pénalité_max = 2):
    '''Retourne un score de différence entre deux lettres.'''
    assert isinstance(lettre_tapée, str)
    assert len(lettre_tapée) == 1
    assert isinstance(lettre_dico, str)
    assert len(lettre_dico) == 1
    score = 0
    # Part 1 : lettres identiques
    if lettre_tapée == lettre_dico:
        return score
    # Part 2 : fautes d'accents
        # Cas 1 : les 2 lettres ont un accent
    elif (lettre_tapée in (list_accents)) & (lettre_dico in (list_accents)):
        if mapping_accent_to_lettre[lettre_tapée] == mapping_accent_to_lettre[lettre_dico]:
            score += pénalité_max/2
        else:
            score += pénalité_max
        # Cas 2:  1 des 2 lettres a un accent
    elif (lettre_tapée in (list_accents)) & (not (lettre_dico in (list_accents))):
        if mapping_accent_to_lettre[lettre_tapée] == lettre_dico:
            score += pénalité_max/2
        else:
            score += pénalité_max
    elif (lettre_dico in (list_accents)) & (not (lettre_tapée in (list_accents))):
        if mapping_accent_to_lettre[lettre_dico] == lettre_tapée:
            score += pénalité_max/2
        else:
            score += pénalité_max
    
    # Part 3 : lettres proches
    elif lettre_dico in (dict_proches_clavier[lettre_tapée]):
        score += pénalité_max/2
    # Part 4 : rien de tout cela, ie lettres non proches sans faute d'accent
    else:
        score += pénalité_max
    return score

def remplacer_a_position(chaine, nouvelle_partie, debut, longueur):
    '''Fonction qui remplace une partie d'une chaine de caractères par une autre'''
    assert isinstance(chaine, str)
    assert isinstance(nouvelle_partie, str)
    assert isinstance(debut, int)
    assert isinstance(longueur, int)
    # Extraire les parties avant et après la section à remplacer
    avant = chaine[:debut]
    apres = chaine[debut + longueur:]
    # Construire la nouvelle chaîne avec la partie remplacée
    chaine_modifiee = avant + nouvelle_partie + apres
    return chaine_modifiee

def mot_sans_permutation_gd(mot_tapé, mot_dico):
    '''Cette fonction retoune le nombre de permutations entre mot_tapé et mot_dico, ainsi que le mot démuni de ses permutations, en parcourant de gauche à droite'''
    # on définit une permutation comme suit : si deux lettres successives sont inversées entre mot_tapé et mot_dico
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    n1 = len(mot_tapé)
    n2 = len(mot_dico)
    n = min(n1, n2)
    mot_perm = str(mot_tapé) #création d'une copie du mot_tapé
    nb_permu = 0
    for i in range (n-1):
        # On parcourt de gauche à droite
        if ((mot_tapé[i] == mot_dico[i+1]) & (mot_tapé[i+1] == mot_dico[i])): #permutation
            mot_perm = remplacer_a_position(mot_perm, mot_tapé[i+1], i, 1)
            mot_perm = remplacer_a_position(mot_perm, mot_tapé[i], i+1, 1)
            nb_permu += 1
    return mot_perm, nb_permu
        
def mot_sans_permutation_dg(mot_tapé, mot_dico):
    '''Cette fonction retoune le nombre de permutations entre mot_tapé et mot_dico, ainsi que le mot démuni de ses permutations, en parcourant de gauche à droite'''
    # on définit une permutation comme suit : si deux lettres successives sont inversées entre mot_tapé et mot_dico
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    n1 = len(mot_tapé)
    n2 = len(mot_dico)
    n = min(n1, n2)
    mot_perm = str(mot_tapé) #création d'une copie du mot_tapé
    nb_permu = 0
    for i in range (n-1):
        
        # Puis de droite à gauche
        if ((mot_tapé[n1-1-i] == mot_dico[n2-i-2]) & (mot_tapé[n1-i-2] == mot_dico[n2-i-1])): #permutation
            mot_perm = remplacer_a_position(mot_perm, mot_tapé[n2-i-2], n1-1-i, 1)
            mot_perm = remplacer_a_position(mot_perm, mot_tapé[n2-i-1], n1-2-i, 1)
            nb_permu += 1
    return mot_perm, nb_permu

def score_mot_letter_diff(mot_tapé, mot_dico, score_max=4, pénalité_max=2, coeff_perm=1):
    assert isinstance(mot_tapé, str)
    assert isinstance(mot_dico, str)
    mot_perm_gd, nb_perm_gd = mot_sans_permutation_gd(mot_tapé, mot_dico)
    mot_perm_dg, nb_perm_dg = mot_sans_permutation_dg(mot_tapé, mot_dico)
    n1 = len(mot_tapé)
    n2 = len(mot_dico)
    n = min(n1, n2)
    score, score_reversed = 0, 0
    for i in range (n):
        score += score_letter_diff(mot_perm_gd[i], mot_dico[i])
        score_reversed += score_letter_diff(mot_perm_dg[n1-i-1], mot_dico[n2-i-1])
    score_final=min(score + coeff_perm*nb_perm_gd, score_reversed + coeff_perm*nb_perm_dg)
    return score_final*score_max/(pénalité_max*n)
    
def score_total(mot_tapé, mot_dico):
    return 1 + score_len(mot_tapé, mot_dico) + score_prem_lettre(mot_tapé, mot_dico) + score_mot_letter_diff(mot_tapé, mot_dico)

def proba_mot_proche(mot_tapé, mot_dico):
    return 1/score_total(mot_tapé, mot_dico)