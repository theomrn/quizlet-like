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

Fr = [["A l'étranger", "selon,suivant", "comptabilité", "précision", "reconnaitre , accuser de recéption",
       "faire de la pub", "conseiller", "diminuer , s'aténuer", "logement", "justifier , expliquer , représenter"]
    , ["comptable", "comptes", "accomplir , atteindre", "en fait", "publicité ,annonce", "publicité", "conseil",
       "toucher,influencer", "avoir les moyens , se permettre", "abordable , pas chère"]
    , ["désolé", "après-vente", "ordre du jour", "but / objectif , vise , avoir un but", "climatisation",
       "allées(magasin),couloir(avion)", "réveil", "permettre", "modifier,changer", "bien que"]
    , ["parmi,entre", "somme,quantité,montant", "mécontent,contrarié", "responsable devant", "répondeur",
       "inquiet,désireux de", "s'excuser", "vêtements", "appel(juridique),attirer", "attirant"]
    , ["appareil", "candidat", "candidature", "demande,postuler,solliciter", "nommmer quelqu'un", "rendez vous",
       "évaluation (de sa performance au travail)", "approbation,assentiment", "se disputer", "dispute"]
    , ["organiser", "arreter quelqu'un", "a partir de", "a condition de", "evaluer", "un atout,un bien",
       "mission,devoir", "aider", "distruteur de billet", "assister a quelque cbose"]
    , ["présence,participation", "vetements", "avocat(a la cour)", "attirer", "vente aux enchères", "disponibilité",
       "disponible", "éviter", "récompenser,prix", "primé,qui gagne un prix"]
    , ["conscient", "conscience", "lot", "avoir du retard", "ne pas manquer de", "avoir le droit a",
       "chargé de,responsable de", "qui vaut", "se comporter", "comportement"]
    , ["bagagiste,groom", "appartenir,aller,se ranger", "affaires,effets personnels", "sous,au-dessous de", "banc",
       "plier", "avantages", "a coté de", "de plus,en plus", "boisson"]
    , ["partial,parti pris", "offrir,faire une enchère de,appel d'offre,enchère", "facture,addition",
       "plan,prototype,blues", "planche,embarquer", "conseil d'administration", "salle de reunion",
       "attacher,verrouiller,écrous", "capot", "reserver"]]

En = [
    ["abroad", "according to", "accounting", "accuracy", "acknowledge", "advertise", "advise", "abate", "accommodation",
     "account for"]
    , ["accountant", "accounts", "achieve", "actually", "ad,advertisement", "advertising", "advice", "affect", "afford",
       "affordable"]
    ,
    ["afraid", "after-sales", "agenda", "aim", "air conditioning", "aisle", "alarm clock", "allow", "alter", "although"]
    , ["among", "amount", "annoyed", "answerable", "answering machine", "anxious", "apologize for", "apparel", "appeal",
       "appealing"]
    , ["appliance", "applicant", "application", "apply for", "appoint", "appointment", "appraisal", "approval", "argue",
       "argument"]
    , ["arrange", "arrest", "as of", "as/so long as", "assess", "asset", "assignment", "assist", "atm", "attend"]
    , ["attendance", "attire", "attorney", "attract", "auction", "availability", "available", "avoid", "award",
       "award-winning"]
    , ["aware", "awareness", "batch", "be behind with something", "be bound", "be entitled to", "be in charge of",
       "be worth", "behave", "behaviour"]
    , ["bellhop,bellman", "belong", "belongings", "below", "bench", "bend", "benefits", "beside", "besides", "beverage"]
    , ["biased", "bid", "bill", "blueprint", "board", "board of directors", "board room", "bolt", "bonnet", "book"]]

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
