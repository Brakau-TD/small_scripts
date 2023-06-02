# Hangman
import sys

letters_found=[]

# dieser Teil ist neu. Mit open("filename.erweiterung") kann man eine Datei öffnen und mit .read() auslesen.
file = open("hangman.txt")
global word
word=file.read()
word = word.lower()
file.close()

loesung=["" for x in word]
letter=[]

def make_blanks(buchstabe="",letter=[]):
    for i,a in enumerate(word):
        if word[i] in letter:
            loesung[i]=buchstabe if loesung[i]=="" else loesung[i]
            print (word[i], end=" ")
        else:
            print("_ ",end="")
    guess_a_letter()

def guess_a_letter():
    pruefe_loesung(loesung)
    abfrage=input("\nYou wanna solve the puzzle? [letter, 'solve [solution]' or 'exit']? ")
    if abfrage.lower()=="exit":
        exit_prg("Oh no!")
    elif abfrage.lower()[:5]=="solve":
        wort_aufloesen(abfrage.lower())
    else:
        print("")
        buchstabe=abfrage.lower()[0]
        letter.append(buchstabe)
        make_blanks(buchstabe,letter)
    
def wort_aufloesen(vorschlag):
    if vorschlag.lower()[6:]==word:
        print(f"{vorschlag.lower()} Was your guess. That is correct!")
        exit_prg("\nYou did very well")
    else:
        print("Hmmmmm")
        return
    
def pruefe_loesung(loesung):
    listToStr = ''.join(map(str, loesung))
    #print("\n",listToStr)
    if listToStr==word:
        exit_prg("You are so utterly amazing!")
    else:
        return

def exit_prg(reason):
    print("")
    print(reason,"\n")
    sys.exit()

make_blanks()