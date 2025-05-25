#Exercice 1

def ecriture_binaire_entier_positif(n):
    vbin = str(n%2)
    n = n // 2
    while n > 0:
        vbin = str(n%2) + vbin
        n = n //2
    return vbin

#Exercice 2

def echange(tab, i, j):
    '''Echange les Ã©lÃ©ments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la mÃ©thode du tri Ã  bulles.'''
    n = len(tab)
    for i in range(n-1): 
        for j in range(n-i-1): 
            if tab[j] > tab[j+1]: 
                echange(tab, j, j+1)


#Exercice 1

#Exercice 2