# Anton Blank och Simon Nilsson 11/10/2022
"""
1.
a. 2 b. 1 c. I main funktionen d. 0 e. 0 f. längst ner i koden

2.



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

#meter per enhet
meter_yard = float(0.9144)
meter_feet = float(0.3048)
meter_inch = float(0.0254)

#enhet per meter
yard_meter = float(1.094)
feet_meter = float(3.28)
inch_meter = float(39.37)

unit_list = ["yard", "feet", "inch"]

#Funktion som sätter värdet på faktorn beroende på vilken enhet som användaren vill ha och printar tabellen.
def info():
	print("En yard är 0.9144 meter, en feet är 0.3048 och en inch är 0.0254 meter, för att konvertera från meter till en annan enhet multiplicerar vi antalet meter med antal meter per enhet (yard, feet eller inch).")
#Frågar användaren vilken längdenhet och hur många produkter hen vill ha i tabellen och åkallar printtable funktionen.

def unit_table():
		chosen_unit = str(input("Would you like to see the table for yard, feet or inch?: "))
		i =	int(input("How many products do you want?: "))
		#kollar om enheten finns i listan
		if chosen_unit.lower() in unit_list:
			print("=============")
			print("Table of " + chosen_unit)
			print("=============")

			if chosen_unit == "yard":
				unit_meter = yard_meter

			elif chosen_unit == "feet":
				unit_meter = feet_meter
			else:
				unit_meter = inch_meter

			# printar tabellen
			for t in range(1, i + 1):
				print(t, "meter är", unit_meter * t, chosen_unit)
		else:
			print("Chosen unit not found.")

#skapar en slumpmässig int mellan 0 och 10, konverterar det till den valda enheten och låter sedan användaren svara, är svaret inom 10% felmarginal är svaret rätt.
def guessing_game():
	chosen_unit = str(input("What unit would you like to guess? Yard, feet or inch?: "))
	if chosen_unit.lower() in unit_list:
		tries = 1
		i = random.randint(1, 10)
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
				if guess > (i*unit_meter*0.9) and guess < (i*unit_meter*1.1):
					print("Right answer! It took", tries, "tries!")
					break
				else:
					print("Nope, try again!")
					tries += 1

			except:
				print("Wrong datatype!")
	else:
		print("Chosen unit not found.")
#Frågar användaren om vilket program hen vill använda.

def main():
	while True:
		program = str(input("Would you like to see the unit table, the guessing game? or info: "))
		if program.lower() == "unit table":
			unit_table()
		elif program.lower() == "guessing game":
			guessing_game()
		elif program.lower() == "info":
			info()

		else:
			print("Please enter guessing game, unit table or info")

main()
"""
Test:

Info: 
Programmet printade följande:
En yard är 0.9144 meter, en feet är 0.3048 och en inch är 0.0254 meter, för att konvertera från meter till en annan enhet multiplicerar vi antalet meter med antal meter per enhet (yard, feet eller inch).
Funkar som det ska.

Unit table:

Yard:
Programmet printade följande:
=============
Table of yard
=============
1 meter är 1.094 yard
2 meter är 2.188 yard
3 meter är 3.282 yard
4 meter är 4.376 yard
5 meter är 5.470000000000001 yard

Feet:
Programmet printade följande:
=============
Table of feet
=============
1 meter är 3.28 feet
2 meter är 6.56 feet
3 meter är 9.84 feet
4 meter är 13.12 feet
5 meter är 16.4 feet

Inch:
Programmet printade följande:
=============
Table of inch
=============
1 meter är 39.37 inch
2 meter är 78.74 inch
3 meter är 118.10999999999999 inch
4 meter är 157.48 inch
5 meter är 196.85 inch

Guessing game:

Yard:
What is 6 meters in yard ?:
2
Nope, try again!
What is 6 meters in yard ?:
6
Right answer! It took 2 tries!

Feet:
What is 8 meters in feet ?:
2
Nope, try again!
What is 8 meters in feet ?:
24
Right answer! It took 2 tries!

Inch:
What is 2 meters in inch ?:
2
Nope, try again!
What is 2 meters in inch ?:
80
Right answer! It took 2 tries!
"""