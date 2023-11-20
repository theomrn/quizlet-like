from random import *

Fr = ["Comptabilité","s'ennyer,ennuyeux","A destination de","Frein,Freiner","Succursale","Marque (d'un produit)","tout neuf","pause,casser","Tomber en panne","Cambrioler,cambriolage"
    , "percer","découverte,percée","porte-document,attaché-case","baisser","avancer","sortir,lancer,faire paraître","élever (un enfant)","ADSL","diffiser,diffusion","courtier"
    , "balai","feuilleter,parcourir","en gros (vente)","boucher","placard","appeler,un appel","rappeler au telephone","annuler","annuler2","Annulation"
    , "ne pas s'empecher","détester,ne pas supporter","continuer à","réaliser,faire","attraper","fournir la nourriture,s'adresser a","traiteur","restauration,buffet","chauffage central","directeur général"
    , "citoyen","citoyenneté,nationalité","présider","president","faire payer,frais","accuser,inculper","tableau,courbe graphique","pas cher","verifier,controler","compte courant"
    , "se présenter à l'enregistrement","regler sa note et rendre la chambre d'hotel","nourrice","hâcher","revendication,reclamation,declaration de sinistre","degager,defricher","employé","intelligent","fermer définitivement","monter,grimper"
    , "s'écrouler,s'éffondrer","baisser","sortir","sugir,apparaitre","avoir/trouver/penser à","pub à la radio/tv","engagement","trajet,voyager(tous les jours)","banlieusard(qui fait la navette)","concurrence"
    , "concurrent","se plaindre","plainte","achèvement,aboutissement","gratuit","conforme à","se soumettre,respecter,etre conforme à","inquiet","mener","se conformer à"
    , "feliciter quelqu'un","envoi","travaux","récipient","entrepeneur","comptoir","quelques","coursier","fomation","couverture"
    , "artisant","se planter,s'effondrer","equipe,equipage","culture,recolte","foule","bondé,plein de gens","croisière","monnaie,devise","actuel,actuellement,en ce moment","client"]

En = ["book-keeping","bore,boring","bound","brake","branch","brand name","brand new","break","break down","break in"
    ,"break into","breakthrough","briefcase","bring down","bring forward","bring out","bring up","broadband","broadcast","broker"
    ,"broom","browse","bulk","butcher","cabinet","call","call back","call off","cancel","cancelation"
    ,"can't help","can't stand","carry on","carry out","catch","cater","caterer","catering","central heating","ceo"
    ,"citizen","citizenship","chair","chairman","charge","charge somebody with something","chart","cheap","check","checking account"
    ,"check in","check out","childminder","chop","claim","clear","clerk","clever","close down","climb"
    ,"collapse","come down","come out","come up","compe up with","commercial","commitment","commute","commuter","competition"
    ,"competitor","complain","complait","completion","complimentary","compliant with","comply with","concerned","conduct","conform"
    ,"congratulate","consignment","construction","container","contractor","counter","couple","courier","course","coverage"
    ,"craftman,craftmen","crash","crew","crop","crowd","crowded","cruise","currency","current","customer"]


"""
Debug
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

def ajouterMot(En,Fr):
    mot = []
    while (len(mot) < 100):
        i = randint(0, len(En)-1)
        mot.append((En[i],Fr[i]))
        del En[i]
        del Fr[i]
    return mot

def test(En,Fr):
    score = 0
    total = 0
    mot = ajouterMot(En,Fr)
    print("pour stoper la boucle mettre -1")
    reponse = ""
    while (reponse != "-1"):
        i = randint(0,len(mot)-1)
        print(mot[i][1], " ?")
        reponse = input()
        if (mot[i][0] != reponse):
            print("la bonne réponse est : ", mot[i][0])
            print("")
            total += 1
        else:
            print("bien joué ! \n")
            del mot[i]
            score += 1
            total += 1
    print("fin du programme")
    print("vous avez fais ", score, " / ", total)

def apprendre(En, Fr):
    aReviser = [0 for i in range(len(En))]
    print("pour stoper la boucle mettre -1")
    reponse = ""
    score = 0
    total = 0
    while (reponse != "-1"):
        i = randint(0,len(En)-1)
        print(Fr[i], " ?")
        reponse = input()
        if (En[i] != reponse):
            print("la bonne réponse est : ", En[i])
            print("")
            total+=1
        else:
            print("bien joué ! \n")
            aReviser[i] += 1
            score += 1
            total += 1
            if(aReviser[i] == 3):
                del aReviser[i]
                del En[i]
                del Fr[i]
            if (len(aReviser)==0):
                break
    print("fin du programme")
    print("vous avez fais ",score," / ",total)
    print("")
    if(len(aReviser)!=0):
        print("mot a reviser :")
        for i in range(0,len(aReviser)):
            print(En[i]," qui veux dire ",Fr[i])


print("voulez vous apprendre ou faire un test ?")
rep = int(input("1 pour apprendre et 2 pour reviser \n"))

if rep == 1:
    apprendre(En,Fr)
else :
    test(En,Fr)