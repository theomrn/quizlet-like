from random import *

Fr = [["annonce","qui en a assez de","s'excuser de","responsable de","payer","agressivement","peu soucieux de","se renseigner sur","adjacent","ajuster"]
      ,["rappeler quelque chose a quelqu'un","ajustement","rire de","admirer","faché de/avec","admettre","avancé","poser sa candidature","admettre","avancé"]
      ,[]]

En = [["annoucement","tired of","apologize for","responsible for","pay for","aggresively","careless about","ask about","adjacent","adjust"]
      ,["remind somebody of","adjustement","laught at","admire","angry at","admit","advanced"]
      ,[]]
print(len(En)==len(Fr))

"""
def ajouterMot():
    mot = []
    while (len(mot) <= 10):
        i = randint(0, 9)
        j = randint(0, len(En[i]) - 1)
        if (Fr[i][j], En[i][j]) not in mot:
            mot.append((Fr[i][j], En[i][j]))
    return mot


continuer = "oui"
manche = 1
aReviser = []
score = 0

while (continuer == "oui"):
    mot = []
    mot = ajouterMot()
    for i in range(0, 10):
        print(mot[i][0], " ?")
        reponse = input()
        if (mot[i][1] != reponse):
            print("la bonne réponse est : ", mot[i][1])
            print("")
            aReviser.append(mot[i])
        else:
            print("bien joué ! \n")
            score += 1
    print(score, "/", 10 * manche)
    manche += 1
    if score != 10:
        print("vous devez reviser : \n")
        for k in range(0, len(aReviser)):
            print(aReviser[k][1], " qui veux dire ", aReviser[k][0])
    print("")
    continuer = input("voulez vous continuer ? (oui pour continuer) ")
"""