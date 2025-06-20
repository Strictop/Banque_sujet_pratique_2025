# %%
def tri_selection(tab : list) -> list:

    n = len(tab)
    cache = 0
    for i in range(n):
        val_min = tab[i]
        indice = i
        for j in range(i,n): # fait une recherche de 0 à n, puis 1 à n...
            if tab[j] < val_min:
                val_min = tab[j]
                indice = j
        
        # partie d'intervertion
        cache = tab[i]
        tab[i] = tab[indice]
        tab[indice] = cache
        
    return tab



# %%
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 9: 
        compteur = compteur + 1
        if nb_mystere > nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere) 
        print("Nombre d'essais: ", compteur) 
    else:
        print ("Perdu ! Le nombre était ", nb_mystere) 


# %%
