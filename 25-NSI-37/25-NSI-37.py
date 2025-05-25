

#Exercice 1

def gb_vers_entier(tab):
    s = 0
    n = len(tab)
    for i in range(n):
        v = tab[n - 1 - i]
        if v :
            s = s + 2**i
    return s

#Exercice 2

def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] 
        # la variable j sert Ã  dÃ©terminer 
        # oÃ¹ placer la valeur Ã  ranger
        j = i 
        # tant qu'on n'a pas trouvÃ© la place de l'Ã©lÃ©ment Ã 
        # insÃ©rer on dÃ©cale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]: 
            tab[j] = tab[j-1]
            j = j - 1 
        tab[j] = valeur_insertion


