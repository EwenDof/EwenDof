# Nom du programme : arbo_robot.py
# Auteur: DECOTE Ewen
# Nouvelle structure de l'arborescence Roboguide
roboguide_arbo = {
	"Parts": [  # "Parts" remplace "Element"
		("Cadre", 0),
		("Triangle", 0),
		("TubeInf", 0),
		("TubeSup", 0)
	],
	"Fixtures": [
		("convTriangle", 0),
		("convTubeInf", 0),
		("convTubeSup", 0),
		("posteSoudage", 0)
	],
	"Machines": [
		("convEvac", 0)
	],
	"RobotControllers": [
		("ARCMate100iD", 0),
		("PositionerHollowType300", 0)
	]
}

# ===========================================================Fonction pour afficher l'arborescence===========================================================
def afficher_arborescence(arbo):
	for idx, (type_objet, elements) in enumerate(arbo.items()):  
		print(f"{idx}. {type_objet}:")
		for idx_element, (nom_element, prix) in enumerate(elements):  
			print(f"   [{idx_element}] {nom_element} (Prix : {prix} €)")

# ===========================================================Fonction pour demander les prix d'un type spécifique============================================
def saisir_type(arbo):
	# Affiche les types disponibles
	print("\n--- Choisissez un type pour gérer ses éléments ---")
	for idx, type_objet in enumerate(arbo.keys()):
		print(f"{idx}. {type_objet}")
	
	# Demande à l'utilisateur de choisir un type
	type_choisi = int(input("Entrez l'index du type à modifier : "))
	type_objet = list(arbo.keys())[type_choisi]
	print(f"\nVous avez choisi : {type_objet}")
	
	elements = arbo[type_objet]
	
	while True:
		print("\n--- Gestion des éléments ---")
		print(f"Éléments actuels dans {type_objet} :")
		for idx_element, (nom_element, prix) in enumerate(elements):
			print(f"   [{idx_element}] {nom_element} (Prix : {prix} €)")

		print("\nOptions :")
		print("1. Ajouter un nouvel élément")
		print("2. Modifier un élément existant (Le nom et le prix)")
		print("3. Supprimer un élément")
		print("4. Ajouter un prix")
		print("5. Retour au menu principal")

		choix = int(input("Entrez votre choix (1-5) : "))

		if choix == 1:  # Ajouter un nouvel élément
			nom_nouvel_element = input("Entrez le nom du nouvel élément : ")
			prix_nouvel_element = float(input(f"Entrez le prix de {nom_nouvel_element} : "))
			elements.append((nom_nouvel_element, prix_nouvel_element))
			print(f"Élément '{nom_nouvel_element}' ajouté avec un prix de {prix_nouvel_element:.2f} €.")
		
		elif choix == 2:  # Modifier un élément existant
			idx_element = int(input("Entrez l'index de l'élément à modifier : "))
			if 0 <= idx_element < len(elements):
				nom_actuel, prix_actuel = elements[idx_element]
				nouveau_nom = input(f"Entrez un nouveau nom pour {nom_actuel} (laisser vide pour conserver) : ")
				nouveau_prix = input(f"Entrez un nouveau prix pour {nom_actuel} (actuel : {prix_actuel}, laisser vide pour conserver) : ")
				
				nouveau_nom = nouveau_nom if nouveau_nom else nom_actuel
				nouveau_prix = float(nouveau_prix) if nouveau_prix else prix_actuel
				
				elements[idx_element] = (nouveau_nom, nouveau_prix)
				print(f"Élément modifié : {nouveau_nom} (Prix : {nouveau_prix:.2f} €).")
			else:
				print("Index invalide.")

		elif choix == 3:  # Supprimer un élément
			idx_element = int(input("Entrez l'index de l'élément à supprimer : "))
			if 0 <= idx_element < len(elements):
				nom_element, _ = elements.pop(idx_element)
				print(f"Élément '{nom_element}' supprimé.")
			else:
				print("Index invalide.")

		elif choix == 4:  # Ajouter un prix
			idx_element = int(input("Entrez l'index de l'élément à ajouter un prix : "))
			if 0 <= idx_element < len(elements):
				nom_element, prix_actuel = elements[idx_element]
				nouveau_prix = float(input(f"Entrez un prix pour {nom_element} : "))
				elements[idx_element] = (nom_element, nouveau_prix)
				print(f"Prix ajouté pour {nom_element} : {nouveau_prix:.2f} €.")
			else:
				print("Index invalide.")
		
		elif choix == 5:  # Retour au menu principal
			print("Retour au menu principal.")
			break

		else:
			print("Choix invalide. Réessayez.")

# ===========================================================Fonction pour calculer le total=================================================================
def calculer_total(arbo):
	total = 0
	for elements in arbo.values():  # "éléments" au lieu de "objets"
		for _, prix in elements:
			total += prix
	return total

# ===========================================================Fonction principale=============================================================================
def main():
	while True:
		print("\n--- Arborescence de la cellule Roboguide ---")
		afficher_arborescence(roboguide_arbo)

		print("\nChoisissez une option:")
		print("1. Saisir un type")
		print("2. Voir le prix total de la BOM")
		print("3. Quitter")

		choix = int(input("Entrez votre choix (1-3): "))
		
		if choix == 1:
			saisir_type(roboguide_arbo)
		elif choix == 2:
			total = calculer_total(roboguide_arbo)
			print(f"\nLe prix total de la BOM est : {total:.2f} €")
		elif choix == 3:
			total = calculer_total(roboguide_arbo)
			print(f"\nLe prix total de la BOM est : {total:.2f} €")			
			print("Programme terminé.")
			break
		else:
			print("Choix invalide, essayez à nouveau.")

if __name__ == "__main__":
	main()
