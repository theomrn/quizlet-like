from random import *
"""from tkinter import *

fenetre = Tk()

fenetre.title("anglais")
fenetre.geometry("600x600")
fenetre.minsize(200, 200)
fenetre.config(background='white')

label_title = Label(fenetre, text="test")
label_title.pack()

fenetre.mainloop()
"""

Fr = [["A l'étranger","selon,suivant","comptabilité","précision","reconnaitre , accuser de recéption","faire de la pub","conseiller","diminuer , s'aténuer","logement","justifier , expliquer , représenter"]
      ,["comptable","comptes","accomplir , atteindre","en fait","publicité ,annonce","publicité","conseil","toucher,influencer","avoir les moyens , se permettre","abordable , pas chère"]
      ,["désolé","après-vente","ordre du jour","but / objectif , vise , avoir un but","climatisation","allées(magasin),couloir(avion)","réveil","permettre","modifier,changer","bien que"]
      ,[]
      ,[]
      ,[]
      ,[]
      ,[]
      ,[]
      ,[]]

En = [["abroad","according to","accounting","accuracy","acknowledge","advertise","advise","abate","accommodation","account for"]
      ,["accountant","accounts","achieve","actually","ad,advertisement","advertising","advice","affect","afford","affordable"]
      ,["afraid","after-sales","agenda","aim","air conditioning","aisle","alarm clock","allow","alter","although"]
      ,[]
      ,[]
      ,[]
      ,[]
      ,[]
      ,[]
      ,[]]

for i in range(0,9):
        if (not(len(En[i]) == len(Fr[i]))):
            print(i , len(En[i]), len(Fr[i]))

s = d = 0
for i in range(0,9):
      s += len(En[i])
      d += len(Fr[i])

if (s != 100 or d != 100):
      print(s,d)

"""
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
"""