from banque.pret import info_client

while True:
    print("\n🏦 Bienvenue à la Banque pour faire un prêt")
    print("1️⃣  Demander un prêt")
    print("2️⃣  Avoir le document de prêt")
    print("3️⃣  Quitter")
    print("")
    print("👉 Veuillez choisir une option (1, 2, 3)")
    choice = input("Votre choix: ")

    if choice == "1":
        print("✅ Vous avez choisi de demander un prêt.")
        # 👉 Code pour demander un prêt ici
        nom = input("Entrez votre nom: ")
        age = input("Entrez votre âge: ")
        montant = input("Entrez le montant demandé: ")
        taux = input("Entrez le taux d'intérêt: ")
        duree = input("Entrez la durée du prêt (en mois): ")
        # Appel de la fonction info_client
        info_client(nom, age, montant, taux, duree)
        print("✅ Votre demande de prêt a été enregistrée.")

    elif choice == "2":
        print("📄 Vous avez choisi d'obtenir le document de prêt.")
        # 👉 Code pour générer/afficher le document ici

    elif choice == "3":
        print("")
        print("👋 Merci d'avoir utilisé notre service. Au revoir !")
        break

    else:
        print("❌ Choix invalide. Veuillez réessayer.")
