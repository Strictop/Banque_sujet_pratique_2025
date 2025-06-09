# Exercice 1
#%%

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)




#%%
def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(notes)): 
        if notes[i] == note_maxi: # si on trouve un eleve avec la meme note maximale
            meilleurs_eleves.append(eleves[i])  # on l'ajoute a la liste d'eleve
        elif notes[i] > note_maxi: 
            note_maxi = notes[i] 
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)



# %%
