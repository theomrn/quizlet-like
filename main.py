from random import *
from tkinter import *
"""
fenetre = Tk()

label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()"""


Fr = [["annonce","qui en a assez de","s'excuser de","responsable de","payer","agressivement","peu soucieux de","se renseigner sur","adjacent","ajuster"]
      ,["rappeler quelque chose a quelqu'un","ajustement","rire de","admirer","faché de/avec","admettre","avancé","poser sa candidature","candidat","chaine"]
      ,["adherence","capasité","adherent","abordable","demander","agenda","tenir à","agent","agression","adhérer"]
      ,["désolé de","désolé de","allouer","attendre","catégorie","alternative","adresse","content de","annuelment","anxiété"]
      ,["anxieux","certain de","appétit","inquiet au sujet de","rire de","application","appliquer","parler de","apprécier","qui connait bien"]
      ,["appréhensif","content de","apprenti","aller avec","approche","s'occuper de","arranger","appartenir à","arrangement","contre,opposé à"]
      ,["aspect","similaire à","assembler","écouter","assistance","attendre avec impatience","associer","parler à","assurance","dépendre de"]
      ,["assurer","intéressé par","attitude","réussir","attirer","abondant","attirant","accepter","attrayant","acceptable"]
      ,["audience","accès","accessibles","autoriser","automatique","accomodant","automatiquement","accompagner","automatisation","accomplir"]
      ,["base","accomplissement","bénéfique","accumuler","accumulation","breuvage","budget","acquérir","calcul","action"]]

En = [["annoucement","tired of","apologize for","responsible for","pay for","aggresively","careless about","ask about","adjacent","adjust"]
      ,["remind somebody of","adjustement","laught at","admire","angry at","admit","advanced","apply for","candidate","chain"]
      ,["adherence","capasity","adherent","affordable","ask for","agenda","care for","agent","aggression","adhere"]
      ,["sorry about","sorry for","allocate","wait for","category","alternative","addresse","happy about","annualy","anxiety"]
      ,["anxious","sure about","appetite","worried about","laught about","application","apply","talk about","appreciate","familiar with"]
      ,["apprehensive","happy with","apprentice","belong with","approach","deal with","arrange","belong to","arrangement","opposed to"]
      ,["aspect","similar to","assemble","listen to","assist","look forward to","associate","talk to","assurance","depend on"]
      ,["assure","insit in","attitude","suceed in","attract","abundant","attraction","accept","attractive","acceptable"]
      ,["audience","access","accessible","authorize","automatic","accommodating","automatically","accompany","automation","accomplish"]
      ,["base","accomplishment","beneficial","accumulate","accumulation","beverage","budget","acquerire","calculation","action"]]


def ajouterMot(connu):
    mot = []
    if (len(connu)<90):
        while (len(mot) <= 10):
            i = randint(0, 9)
            j = randint(0, len(En[i]) - 1)
            if (Fr[i][j], En[i][j])  not in mot and (Fr[i][j], En[i][j]) not in connu:
                mot.append((Fr[i][j], En[i][j]))
    else :
        while (len(mot) <= 100-len(connu)):
            i = randint(0, 9)
            j = randint(0, len(En[i]) - 1)
            if (Fr[i][j], En[i][j])  not in mot and (Fr[i][j], En[i][j]) not in connu:
                mot.append((Fr[i][j], En[i][j]))
    return mot


continuer = "oui"
manche = 1
aReviser = []
score = 0
connu = []

while (continuer == "oui"):
    mot = []
    mot = ajouterMot(connu)
    for i in range(0, 10):
        print(mot[i][0], " ?")
        reponse = input()
        if (mot[i][1] != reponse):
            print("la bonne réponse est : ", mot[i][1])
            print("")
            if (mot[i] not in aReviser):
                aReviser.append(mot[i])
        else:
            print("bien joué ! \n")
            connu.append(mot[i])
            score += 1
    print((score/manche)*10, "%")
    manche += 1
    print("")
    continuer = input("voulez vous continuer ? (oui pour continuer) \n")

print("vous devez reviser : \n")
for k in range(0, len(aReviser)):
    print(aReviser[k][1], " qui veux dire ", aReviser[k][0])