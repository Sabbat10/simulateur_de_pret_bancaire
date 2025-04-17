# information client
def info_client(nom, age, montant, taux, duree):
    
    print("")
    print("📋 Informations du client:")
    print("Nom:", nom)
    print("Age:", age)
    print("Montant demandé:", montant)
    print("Taux d'intérêt:", taux, "%")
    print("Durée du prêt:", duree, "mois")
    return nom, age, montant, taux, duree