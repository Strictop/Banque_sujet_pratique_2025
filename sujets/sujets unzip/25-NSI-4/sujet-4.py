# ex1
#%%
def ecriture_binaire_entier_positif(n):
    if n <= 1:
        return str(n)
    return ecriture_binaire_entier_positif(n // 2) + str(n%2)

#%%
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(len(tab)-1): 
        for j in range(len(tab) - i - 1): 
            if tab[j] > tab[j+1]:
                echange(tab, j, j + 1) 



# %%
