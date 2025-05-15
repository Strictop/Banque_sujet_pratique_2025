def ecriture_binaire_entier_positif(n):
    binaire=""
    while n>0:
        binaire= str(n%2) + binaire
        n=n//2
    return binaire

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ... 
    tab[i] = ... 
    tab[j] = ... 

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(...): 
        for j in range(...): 
            if ... > ...: 
                echange(tab, j, ...) 


