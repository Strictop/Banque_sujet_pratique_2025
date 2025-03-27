# %%
def voisins_entrants(adj,x):
    '''
    Renvoie une liste contenant les voisins entrants du sommet x, c-à-d les sommets
    y tels qu'il existe une arête de y vers x
    '''
    L = list()
    # on va chercher à travers la liste d'adjacence lesquelles ont x comme voisin
    for i in range(len(adj)):
        if x in adj[i]:
            L.append(i)

    return L

voisins_entrants([[1, 2], [2], [0], [0]], 1)
# %%

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1

    for i in range(1,len(s)): 
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat

nombre_suivant('13498249')
# %%
