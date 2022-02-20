import random
import os


def programme():
	global longueur


	if longueur == 3:
		print(random.randrange(999))
		restart = input("Voulez vous regénérer un code PIN à trois chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 4:
		print(random.randrange(9999))
		restart = input("Voulez vous regénérer un code PIN à quatres chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 5:
		print(random.randrange(99999))
		restart = input("Voulez vous regénérer un code PIN à cinq chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 6:
		print(random.randrange(999999))
		restart = input("Voulez vous regénérer un code PIN à six chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 7:
		print(random.randrange(9999999))
		restart = input("Voulez vous regénérer un code PIN à septs chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 8:
		print(random.randrange(99999999))
		restart = input("Voulez vous regénérer un code PIN à huits chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 9:
		print(random.randrange(999999999))
		restart = input("Voulez vous regénérer un code PIN à neufs chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")


	if longueur == 10:
		print(random.randrange(9999999999))
		restart = input("Voulez vous regénérer un code PIN à dix chiffres ? (oui ou non) : ")
		if restart == "oui":
			start()
		else :
			os.system("cls")
			os.system("color 1")
			print("A une prochaine fois peut être ;)")



def start():
	global longueur

	if longueur == 3:
		programme()
	elif longueur == 4:
		programme()
	elif longueur == 5:
		programme()
	elif longueur == 6:
		programme()
	elif longueur == 7:
		programme()
	elif longueur == 8:
		programme()
	elif longueur == 9:
		programme()
	elif longueur == 10:
		programme()
	else:
		os.system("cls")
		os.system("color 4")
		print("Veuillez inscrire un chiffre entre 1 et 10 !")
		print("FIN DU PROGRAMME !")





os.system("cls")
os.system("color a")
print("Voici les longueurs disponibles : 3, 4, 5, 6, 7, 8, 9, 10")
print(" ")
longueur = int(input("Choisissez la longueur du code PIN (entre 3 et 10) : "))

start()
