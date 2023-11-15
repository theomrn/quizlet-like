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

Fr = [["Comptabilité","s'ennyer,ennuyeux","A destination de","Frein,Freiner","Succursale","Marque (d'un produit)","tout neuf","pause,casser","Tomber en panne","Cambrioler,cambriolage"]
    , ["percer","découverte,percée","porte-document,attaché-case","baisser","avancer","sortir,lancer,faire paraître","élever (un enfant)","ADSL","diffiser,diffusion","courtier"]
    , ["balai","feuilleter,parcourir","en gros (vente)","boucher","placard","appeler,un appel","rappeler au telephone","annuler","annuler2","Annulation"]
    , ["ne pas s'empecher","détester,ne pas supporter","continuer à","réaliser,faire","attraper","fournir la nourriture,s'adresser a","traiteur","restauration,buffet","chauffage central","directeur général"]
    , ["citoyen","citoyenneté,nationalité","présider","president","faire payer,frais","accuser,inculper","tableau,courbe graphique","pas cher","verifier,controler","compte courant"]
    , ["se présenter à l'enregistrement","regler sa note et rendre la chambre d'hotel","nourrice","hâcher","revendication,reclamation,declaration de sinistre","degager,defricher","employé","intelligent","fermer définitivement","monter,grimper"]
    , ["s'écrouler,s'éffondrer","baisser","sortir","sugir,apparaitre","avoir/trouver/penser à","pub à la radio/tv","engagement","trajet,voyager(tous les jours)","banlieusard(qui fait la navette)","concurrence"]
    , ["concurrent","se plaindre","plainte","achèvement,aboutissement","gratuit","conforme à","se soumettre,respecter,etre conforme à","inquiet","mener","se conformer à"]
    , ["feliciter quelqu'un","envoi","travaux","récipient","entrepeneur","comptoir","quelques","coursier","fomation","couverture"]
    , ["artisant","se planter,s'effondrer","equipe,equipage","culture,recolte","foule","bondé,plein de gens","croisière","monnaie,devise","actuel,actuellement,en ce moment","client"]]

En = [["book-keeping","bore,boring","bound","brake","branch","brand name","brand new","break","break down","break in"]
    ,["break into","breakthrough","briefcase","bring down","bring forward","bring out","bring up","broadband","broadcast","broker"]
    ,["broom","browse","bulk","butcher","cabinet","call","call back","call off","cancel","cancelation"]
    ,["can't help","can't stand","carry on","carry out","catch","cater","caterer","catering","central heating","ceo"]
    ,["citizen","citizenship","chair","chairman","charge","charge somebody with something","chart","cheap","check","checking account"]
    ,["check in","check out","childminder","chop","claim","clear","clerk","clever","close down","climb"]
    ,["collapse","come down","come out","come up","compe up with","commercial","commitment","commute","commuter","competition"]
    ,["competitor","complain","complait","completion","complimentary","compliant with","comply with","concerned","conduct","conform"]
    ,["congratulate","consignment","construction","container","contractor","counter","couple","courier","course","coverage"]
    ,["craftman,craftmen","crash","crew","crop","crowd","crowded","cruise","currency","current","customer"]]


"""
for i in range(0,10):
        if (not(len(En[i]) == len(Fr[i]))):
            print(i , len(En[i]), len(Fr[i]))

s = d = 0
for i in range(0,10):
      s += len(En[i])
      d += len(Fr[i])

if (s != 100 or d != 100):
      print(s,d)
"""


def ajouterMot(connu):
    mot = []
    if (len(connu) < 90):
        while (len(mot) <= 10):
            i = randint(0, 9)
            j = randint(0, len(En[i]) - 1)
            if (Fr[i][j], En[i][j]) not in mot and (Fr[i][j], En[i][j]) not in connu:
                mot.append((Fr[i][j], En[i][j]))
    else:
        while (len(mot) <= 100 - len(connu)):
            i = randint(0, 9)
            j = randint(0, len(En[i]) - 1)
            if (Fr[i][j], En[i][j]) not in mot and (Fr[i][j], En[i][j]) not in connu:
                mot.append((Fr[i][j], En[i][j]))
    return mot


continuer = "oui"
manche = 1
aReviser = []
score = 0
connu = []

"""
for i in range(0,10):
    aReviser = aReviser + En[i]
print(aReviser)
"""
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
    print((score / manche) * 10, "%")
    manche += 1
    print("")
    continuer = input("voulez vous continuer ? (oui pour continuer) \n")

print("vous devez reviser : \n")
for k in range(0, len(aReviser)):
    print(aReviser[k][1], " qui veux dire ", aReviser[k][0])