""" a simple Quiz """

print("Herzlich willkommen zum Quiz!")

punkte = 0
antwort = input("Wie wird unsere Schule abgekürzt? ")
if antwort == "GymBla" or antwort == "gymbla":
	print("Richtig!")
	punkte = punkte +1
else:
	print("Leider falsch")

## Das war die leichteste Variante, in diesem Schema können die SuS erstmal ein paar Fragen erstellen
## Dann kann man etwas vereinfachen

punkte = 0
antwort = input("Wie wird unsere Schule abgekürzt?")
if antwort.lower()=="gymbla":
	print("Richtig")
	punkte += 1
else:
	print("Falsch")
	
## oder noch mehr:

fragen = ["Wie wird unsere Schule abgekürzt?", "Wie heißt unser Schulleiter mit Vornamen?"]
antworten = ["gymbla", "michael"]

for i,fragen in enumerate(fragen):
	antwort = input(fragen)
	if antwort.lower()==antworten[i]:
		print("Richtig")
		punkte+=1
	else:
		print("Leider falsch")
		
## oder noch geschickter:
quiz = {
	"Wie wird unsere Schule abgekürzt?": "gymbla",
	"Wie heißt unser Schulleiter mit Vornamen?": "michael"
		}
punkte = 0
for key in quiz:
    a = input(key)
    if a == quiz[key]:
        print("Richtig!")
        punkte+=1
    else:
	    print("leider falsch")
