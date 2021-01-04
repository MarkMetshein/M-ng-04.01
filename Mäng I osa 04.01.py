#Mark Metshein
#IT20
###KT mäng###
####################Smaug####################
import time
import random
import os
from pathlib import Path
#Seaded
name = ""
sleep=2
valik = ""
#goblin atribuudid #võibolla teha paar erinevat koletist ning võitluseks valib random range ühe koletise?
# def Goblin():
#     Kolla = Goblin
#     Jõud = print(random.randrange(4,7))
#     Tase = 1
#     Kaitse = print(random.randrange(1,4))

#troll atribuudid
# def Troll():
#     Kollb = Troll
#     Jõud = print(random.randrange(3.5,7))
#     Tase = 1
#     Kaitse = print(random.randrange(1,4))

#Story
def prolog():
    print("Alustame mänguga!")
    time.sleep(sleep)
    print("Sa sisened kõrtsu tormisel õhtul...")
    time.sleep(sleep)
    print("Seal kuuled lugu draakonist nimega Smaug, kes magab koopas ning valvab aardeid.")
    time.sleep(sleep)
    print("Smaug on terroriseerinud seda linna aastakümneid.")
    time.sleep(sleep)
    kys = input("Kas soovid linna aidata? (jah/ei): ")
    if kys == "jah":
        print("Hea valik!")
        time.sleep(sleep)
    elif kys == "ei":
        print("Kardad? lol")
        time.sleep(sleep)
        print("Mäng läbi!")
        loop == 0

#return 
def Kasutaja():
#     time.sleep(sleep)
    name = input("Sisestage enda nimi: ")
#Kasutaja kontroll, kas on olemas
    time.sleep(sleep)
    #faili otsing
    if Path(name+".txt").is_file():
        #fail on olemas
        print ("Sisestatud kasutaja juba eksisteerib.")
        time.sleep(sleep)
        print("Kasutan olemasoleva kasutaja", name, "andmeid.")
        time.sleep(sleep)
        print("Tere tulemast tagasi, "+name+"!")
        time.sleep(sleep)        
        print("Siin on teie karakteri oskuspunktid: ")
        #Olemasoleva konto andmed
        s = open(name+".txt", 'r').read()
#         s = {'Tase': 1, 'Jõud': 20, 'Kaitse': 5}
#         for key, value in s.items():
#             print(key+":", value)
        print("Tase: "+s[9])
        print("Jõud: "+s[20:22])
        print("Kaitse: "+s[34:35])
    else:
        #faili pole, uue kasutaja tervitamine
        print ("Sisestatud on uus kasutaja.")
        time.sleep(sleep)
        name = name.capitalize()
        print("Tervist, üllas", (name)+"!")
        nimi = name
        Tase = 1
        Jõud = 10
        Kaitse = 5
        time.sleep(sleep)
        print("Hetkel on sul: \nTase: ", Tase, "\nJõud: ", Jõud, "\nKaitse: ", Kaitse)    
        time.sleep(sleep)
        valik = (str(input("Valige, kuhu soovite 10 punkti juurde lisada(Jõud/Kaitse): ")))
    #punktide lisamine
        if valik == "Jõud" or valik == "jõud":
            Jõud = Jõud + 10
#             Kaitse = 5
#             num = (str(Jõud))
#             num2 = (str(Kaitse))
            print("Jõud: 20")
            print("Kaitse: 5")
            print("-------------")
        elif valik == "Kaitse" or valik == "kaitse":
            Jõud = 10
            Kaitse = Kaitse + 10
            print("Jõud: 10")
            print("Kaitse: 15")
            print("-------------")

        time.sleep(sleep)
        print("Kasutaja atribuudid", nimi+".txt faili salvestamine")
        time.sleep(0.9)
        print("Kasutaja fail salvestatud nimega: "+nimi+(".txt"),"desktopile")
        print("-----------------------------------------------------")
        time.sleep(sleep)
#arakteri salvestamine
        oskused = [(nimi),(Tase),(Jõud),(Kaitse)]
        kasutaja1 = {
        "Tase": Tase,
        "Jõud": Jõud,
        "Kaitse": Kaitse
        }

        f = open(nimi+".txt", "w") 
        f.write(str(kasutaja1))
        f.close()
  
def seiklus():
    time.sleep(sleep)
    print("Sa alustad oma teekonda...")
    time.sleep(3)
    valik = input("Linnaväravatest välja astudes läheb rada kaheks, kumma suuna valid?(vasak/parem): ")
    #vasakul on goblinid vms ning paremal on trollid
    if valik == "vasak" or "Vasak":
        print("Valisid vasaku raja.")
    else:
        print("Valisid parema raja.")

def vasak():
    print("Mingi lahe story tekst siia")
    time.sleep(sleep)
    print("Su teele satub ette üks goblin!")
    time.sleep(sleep)
    print("Sul pole muud võimalust, kui temaga võidelda!")

def parem():
    print("Mingi lahe story tekst siia")
    time.sleep(sleep)
    print("Põõsast hüppab välja ühe käega troll!")
    time.sleep(sleep)
    print("Sul pole muud võimalust, kui temaga võidelda!")

#Käivitamine
loop=1
while loop==1:

    Kasutaja()

    seiklus()

    vasak()

    parem()

print("Mäng läbi!")