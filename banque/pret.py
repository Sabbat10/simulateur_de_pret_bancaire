# information client
def info_client(nom, age, montant, taux, duree):
    
    print("")
    print("📋 Informations du client:")
    print("Nom:", nom)
    print("Age:", age)
    print("Montant demandé:", montant)
    print("Taux d'intérêt:", taux,"%")
    print("Durée du prêt:", duree, "mois")
    return nom, age, montant, taux, duree


# calculer les interets

def calcul_interet(montant, taux, duree_mois):
    try:
        montant = float(montant)
        taux = float(taux) / 100  # L'utilisateur entre 5 → converti en 0.05
        duree_mois = int(duree_mois)

        duree_annee = duree_mois / 12
        interet = montant * taux * duree_annee
        montant_total = montant + interet
        mensualite = montant_total / duree_mois

        print("\n📋 Résumé de votre prêt :")
        print(f"🔸 Montant emprunté      : {montant:.2f} €")
        print(f"🔸 Taux d'intérêt        : {taux * 100:.2f} %")
        print(f"🔸 Durée                 : {duree_mois} mois")
        print(f"🔸 Intérêts à payer      : {interet:.2f} €")
        print(f"🔸 Mensualité            : {mensualite:.2f} €")
        print(f"🔸 Total à rembourser    : {montant_total:.2f} €\n")

    except ValueError:
        print("❌ Erreur : Veuillez entrer des valeurs valides.")

