import webbrowser
import atexit
import json

dict = {}

data = open("Autosave.txt", "a+")

@atexit.register
def programClosing():
    with open("Autosave.txt", "w") as file_write:
        json.dump(dict, file_write)

def endGame():
    print("The end")
    webbrowser.open("https://youtu.be/JH642hpJtFs")
    exit()

def Settings():
    print("Geen settings noob")
    webbrowser.open("https://youtu.be/HtTUsOKjWyQ?t=13")

def wrongAwnser():
    print("Wat een noob ben jij!")
    webbrowser.open("https://youtu.be/l60MnDJklnM")
    Vragen()
    

def Vragen(Vraag1, Vraag2, Vraag3, Vraag4, Vraag5, Vraag6, Vraag7, Vraag8):
    Awnser1 = input(Vraag1)
    if Awnser1 == "Gabe the Dog" or Awnser1 == "gabe the dog":
        webbrowser.open("https://youtu.be/Ye6TI_iYEV0")
        dict[Vraag1] = "Gabe the Dog"
    else:
        wrongAwnser()
    Awnser2 = input(Vraag2)
    if Awnser2 == "Ron Jans" or Awnser2 == "ron jans":
        webbrowser.open("https://youtu.be/F4PKT9SBvHA")
        dict[Vraag2] = "Ron Jans"
    else:
        wrongAwnser()
    Awnser3 = input(Vraag3)
    if Awnser3 == "Pablo" or Awnser3 == "pablo":
        webbrowser.open("https://youtu.be/KzkBoUTEzKg")
        dict[Vraag3] = "Pablo"
    else:
        wrongAwnser()
    Awnser4 = input(Vraag4)
    if Awnser4 == "i like ya cut g" or Awnser4 == "I like ya cut g":
        webbrowser.open("https://youtu.be/hRPpgleML1o")
        dict[Vraag4] = "i like ya cut g"
    else:
        wrongAwnser()
    Awnser5 = input(Vraag5)
    if Awnser5 == "Smooth like butter" or Awnser5 == "smooth like butter":
        webbrowser.open("https://youtu.be/Pq301GSRuYM")
        dict[Vraag5] = "Smooth like butter"
    else:
        wrongAwnser()
    Awnser6 = input(Vraag6)
    if Awnser6 == "Nyan cat" or Awnser6 == "nyan cat":
        webbrowser.open("https://youtu.be/QH2-TGUlwu4")
        dict[Vraag6] = "Nyan cat"
    else:
        wrongAwnser()
    Awnser7 = input(Vraag7)
    if Awnser7 == "Lando Norris":
        webbrowser.open("https://youtu.be/kfYOkEIfWwI")
    elif Awnser7 == "Daniel Riccardo":
        webbrowser.open("https://youtu.be/_uPTHKobAAc")
    elif Awnser7 == "James its Valtteri":
        webbrowser.open("https://youtu.be/J2nKdlygIHc?list=LL")
    else:
        wrongAwnser()
    Awnser8 = input(Vraag8)
    if Awnser8 == "Korter" or Awnser8 == "korter":
        webbrowser.open("https://youtu.be/ypSKDY4Jp3g?t=44")
        endGame()
    else:
        wrongAwnser()

def menuChoice():
    Choice = input("Uw keuze \n")
    if Choice == "Spelen":
        print("In dit spel ga je allemaal verschillende memes krijgen. Als je een vraag goed heb krijg je een punt.")
    elif Choice == "Settings":
        Settings()
        return menuChoice()
print("++++++++++++++++++++++++++++++++++++++")
print("The Meme Mind - Official 0.0.1 Beta Version")
print("1. Spelen")
print("2. Settings")
print("++++++++++++++++++++++++++++++++++++++")
menuChoice()

Vragen(Vraag1 = "Welke hond is zo bekend door het blaffen? \n", Vraag2="Welke Nederlandse Internet gekkie is bekend door het woord keukenrol? \n", Vraag3="Bij welke meme springt er iemand van een brug? \n", Vraag4="You Playing minecraft, ", Vraag5="Welke meme is ook wel bekend met boter? \n", Vraag6="Wat is de regenboog kat? \n", Vraag7="Welke F1 meme is erg bekend. \n", Vraag8="Moet deze meme game langer of korter? \n")