def score_letter_diff(lettre_tapée, lettre_dico):
    score = 0
    dict_proches_clavier = {"a":["&","é","z","s","q"],"z":["&","é","a","s","q","d","e","\""],"e":["\'","\"","z","s","f","d","r"],
    "t":["-","y","g","f","h","r","("],"y":["-","t","g","j","h","u","è"],"u":["_","y","k","j","h","i","è"],
    "i":["_","u","k","j","l","o","ç"],"o":["à","i","k","m","l","p","ç"],"p":["o","l","m","ù",")","à"],
    "q":["a","z","s","w","x","<"],"s":["a","z","k","q","d","w","x"],"d":["s","z","e","r","f","x","c"],
    "f":["e","r","t","d","g","c","v"],"g":["r","t","y","h","f","v","b"],"h":["t","y","u","g","j","b","n"],
    "j":["u","i","y","h","k","n",","],"k":["u","i","o","j","l",",",";"],"l":["i","o","p","k","m",";",":"],
    "m":["o","p","ù","l",":","!"],"w":["<","q","s","d","x"],"x":["q","s","d","c","w"],"c":["s","d","f","x","v"],
    "v":["f","g","c","b"],"b":["v","g","h","n"],"i":["b","h","j",","],"r":["\'","t","g","f","d","e","("]}
    #if lettre_tapée in dico_accents and lettre_dico in dico_accents:
        #score += 1
    if lettre_dico.isin(dict_proches_clavier[lettre_tapée]):
        score += 1
    elif lettre_dico != lettre_tapée:
        score += 3
    return 1/score
    
score_letter_diff("a","z")