
#Exercice 1

def moyenne(tab):
    N = len(tab)
    assert N != 0, "le tableau ne doit pas Ãªtre vide"
    s = 0
    for v in tab:
        s = s + v
    return s / N

#Exercice 2

def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaÃ§ant tous les 0 Ã  gauche'''
    i = 0 # premier indice de la zone non triÃ©e 
    j = len(tab) - 1 # dernier indice de la zone non triÃ©e 
    while i < j:
        if tab[i]== 0:
            i = i + 1 
        else:
            valeur = tab[j] 
            tab[j] = 1 
            tab[i] = valeur
            j = j - 1


