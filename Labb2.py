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
yard_meter = float(0.9144)
foot_meter = float(0.3048)
inch_meter = float(0.0254)
#Funktion som sätter värdet på faktorn beroende på vilken enhet som användaren vill ha.
def printtable():
	print("=============")
	print("Table of " + chosen_unit)
	print("=============")
	if chosen_unit == "yard":
		unit_meter = yard_meter

	elif chosen_unit == foot_meter:
		unit_meter = foot_meter
	else:
		unit_meter = inch_meter
	#printar tabellen
	for t in range(1, i+1):
		print(unit_meter*t)

unit_list = ["yard", "foot", "inch"] 
while True:
	#Frågar användaren vilken längdenhet och hur många produkter hen vill ha i tabellen.
	chosen_unit = str(input("Would you like to see the table for yard, foot or inch?: "))
	i =	int(input("How many products do you want?"))
	#kollar om enheten finns i listan
	if chosen_unit.lower() in unit_list:
		printtable()
	else:
		print("Chosen unit not found.")

printtable()