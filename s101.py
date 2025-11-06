# Code de la SAE S101 (uniquement les définitions de fonction)

def nombre_eleves(reponses):
    return len(reponses) / 5

def eleves(reponses):
    e = []
    i = 0
    while i < len(reponses):
        e.append(reponses[i])
        i += 5
    return e

def lecture_reponses(nom_fichier):
    rep = []

    f = open(nom_fichier)
    lignes = f.readlines()
    f.close()

    # Pour chaque ligne
    i = 0
    while i < len(lignes):
        cut = lignes[i].split(":")
        # Ajout du nom
        rep.append(cut[0])
        scores = cut[1].split("/")
        j = 0
        while j < len(scores):
            rep.append(int(scores[j]))
            j += 1
        i += 1
    return rep


def maison(reponses, indice):
    ind_score_max = 0
    
    # Parcours des scores. Chaque score se trouve à l'indice indice + 1
    j = 0
    while j < 4:
        if reponses[indice + 1 + j] > reponses[indice + 1 + ind_score_max]:
            ind_score_max = j
        j += 1
    #ind_score max est un nombre entre 0 et 4 correspondant à la question où l'élève a mis le score maximum
    m = ["Gryffondor", "Serdaigle", "Poufsouffle", "Serpentard"]
    return m[ind_score_max]

def repartition(reponses):
    aff = {}
    i = 0
    while i < len(reponses):
        aff[reponses[i]] = maison(reponses, i)
        i += 5
    return aff

def nb_erreurs(d1, d2):

    nb_erreurs = 0
    
    # Parcours de la liste des élèves
    eleves = list(d1)
    i = 0
    while i < len(d1):
        if d1[eleves[i]] != d2[eleves[i]]:
            nb_erreurs += 1
        i += 1
    return nb_erreurs