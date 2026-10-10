##Exercice Python 04 : Dictionnaires sur les Ventes
ventes = [
    {"produit" : "café", "prix" : 2.5, "quantité" : 120},
    {"produit" : "thé", "prix" : 2.0, "quantité" : 80},
    {"produit" : "jus", "prix" : 3.5, "quantité" : 45}
]

ca_par_produit = {vente["produit"]: vente["prix"] * vente["quantité"] for vente in ventes}
ca_total = sum(ca_par_produit.values())
produit_plus_rentable = max(ca_par_produit, key=ca_par_produit.get)

print(f"{ca_par_produit}")
print(f"Total : {ca_total:.2f} euros")
print(f"Meilleur produit : {produit_plus_rentable}")