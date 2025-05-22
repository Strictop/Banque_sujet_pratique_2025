# %%
def parcours_largeur(arbre):
    
    
    if arbre is None:
        return []
    

    queue = list()
    queue.append(arbre)
    etiquette = []

    while queue != []:
        noeud = queue.pop(0)
        etiquette.append(noeud[1])

        if noeud[0] != None:
            queue.append(noeud[0])
        if noeud[2] != None:
            queue.append(noeud[2])
    
    return etiquette

arbre = ( ( (None, 1, None), 2, (None, 3, None) ),4,( (None, 5, None), 6, (None, 7, None) ) )
parcours_largeur(arbre)



    







# %%
def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if sommes_max[i-1] + tab[i] > sommes_max[i-1]: 
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum] : 
            maximum = i
    return sommes_max[maximum] 



# %%

def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if sommes_max[i-1] + tab[i] > tab[i]: 
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    
    for i in range(n):
        print(sommes_max[i])

# %%
