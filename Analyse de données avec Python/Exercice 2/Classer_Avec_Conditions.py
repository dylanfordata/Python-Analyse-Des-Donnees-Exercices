##Exercice Python 02 : Classer avec des conditions
##Partie 1 : Classer les températures
temperatures = [-3, 0, 15, 31]

for temperature in temperatures:
    if temperature < 0:
        categorie = "gel"
    elif temperature < 15:
        categorie = "froid"
    elif temperature < 25:
        categorie = "doux"
    else:
        categorie = "chaud"

    print(f"{temperature} °C : {categorie}")


##Partie 2 : Année Bissextile
def est_bissextile(annee):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

for annee in [2024, 1900, 2000]:
    if est_bissextile(annee):
        resultat = "bissextile"
    else:
        resultat = "non bissextile"

    print(f"{annee} : {resultat}")
