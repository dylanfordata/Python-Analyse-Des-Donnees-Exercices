##Exercice Python 01 : Variable et Calculs
produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")

# Conversion du prix depuis un texte
prix_texte = "19,90"
prix_ht = float(prix_texte.replace(",", "."))

total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")