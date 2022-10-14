# Anton Blank och Simon Nilsson 11/10/2022
"""
1.
a. 2 b. 1 c. I main funktionen d. 0 e. 0 f. längst ner i koden

2.

def info_yard():
	print("En yard är 0.9144 meter, för att konvertera från meter till yard multiplicerar vi antalet meter med 0.9144.")

info_yard()

antal_meter = float(input("Antal meter?"))
def meter_konverter(meter):
	antal_yard = meter*0.9144
	return antal_yard

def main():

	antal_yard = meter_konverter(meter = antal_meter)
	print(antal_meter, "i yards är", antal_yard)

main()	

3.

def multiplikationstabell():
	n = int(input("Vilken multiplikationstabell?"))
	print()
	print("Multiplikationstabell för", n)
	print("="*27)
	for i in range(1,10):
		print(i*n)
	print()
def main():
	multiplikationstabell()
main()

4. 

import random

def main():
	tal = random.randint(1,10)
	gissning = input("Gissa ett tal mellan 1 och 10: ")
	if gissning == tal:
		print("rätt!")
	else: 
		print("Fel!")
main()

import random

def main():
	tal1 = random.randint(1,10)
	tal2 = random.randint(1,10)
	print(tal1, tal2)
	antal_fel = 1
	while True:
		gissning = int(input("Vad blir produkten?: "))
		if gissning != tal1*tal2:
			print("Fel, försök igen :)")
			antal_fel += 1
		else:
			print("Rätt!, det tog", antal_fel, "gånger")
			break 
main()

"""
import random

yard_meter = float(0.9144)
feet_meter = float(0.3048)
inch_meter = float(0.0254)
#Funktion som sätter värdet på faktorn beroende på vilken enhet som användaren vill ha och printar tabellen.
def printtable(chosen_unit, i):
	print("=============")
	print("Table of " + chosen_unit)
	print("=============")

	if chosen_unit == "yard":
		unit_meter = yard_meter

	elif chosen_unit == "feet":
		unit_meter = feet_meter
	else:
		unit_meter = inch_meter
	
	#printar tabellen
	for t in range(1, i+1):
		print(unit_meter*t, chosen_unit)
		break

unit_list = ["yard", "feet", "inch"] 

#Frågar användaren vilken längdenhet och hur många produkter hen vill ha i tabellen och åkallar printtable funktionen.
def unit_table():
	while True:
		chosen_unit = str(input("Would you like to see the table for yard, feet or inch?: "))
		i =	int(input("How many products do you want?: "))
		#kollar om enheten finns i listan
		if chosen_unit.lower() in unit_list:
			printtable(chosen_unit, i)
		else:
			print("Chosen unit not found.")

#skapar en slumpmässig int mellan 0 och 10, konverterar det till den valda enheten och låter sedan användaren svara, är svaret inom 10% felmarginal är svaret rätt.
def guessing_game():
	chosen_unit = str(input("What unit would you like to guess? Yard, feet or inch?: "))
	tries = 1
	i = random.randint(0, 10)
	while True:
		print("What is", i,"meters in", chosen_unit, "?: ")
		if chosen_unit == "yard":
			unit_meter = yard_meter

		elif chosen_unit == "feet":
			unit_meter = feet_meter
		else:
			unit_meter = inch_meter

		guess = float(input())
		try:
			if guess < (i*unit_meter*0.9) and guess > (i*unit_meter*1.1):
				print("Nope, try again!")
				tries += 1
			else:
				print("Right answer! It took", tries, "tries!")
				break 
				
		except: 
			print("Wrong datatype!")

#Frågar användaren om vilket program hen vill använda.
while True:
	program = str(input("Would you like to see the unit table or the guessing game?: "))
	if program.lower() == "unit table":
		unit_table()
	elif program.lower() == "guessing game": 
		guessing_game()
	else:
		print("Please enter guessing game or unit table")

"""
Vi har testat att köra programmet och hittade inga buggar.
"""