# %%

# ex1
def voisins_entrants(adj, x):
    voisins = []
    for y in range(len(adj)):
        if x in adj[y]:
            voisins.append(y)
    return voisins


def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += f'{compte}{chiffre}' 
            chiffre = s[i]
            compte = 1
    lecture_chiffre = f'{compte}{chiffre}'
    resultat += lecture_chiffre
    return resultat

nombre_suivant('1211')