from random import *

Fr1 = ["(taux de) présence du personnel" , "dédaigneux / condéscendant","éloge","évaluateur, expert","motivation","acceptant / contestant"
       ,"alors que , tandis que","par la présente","intérimaire","prestataire","poste vacant"]

En1 = ["Staff attendance","dismissive","praise","assessor","incentive","agreeing"
       ,"whereas","hereby","temp","contractor","vacancy"]

Fr2 = ["main d'oeuvre, effectifs","embaucher","réduire les effectifs","licencier pour motif économique","donner son preavis","renvoyer","licencié"
       ,"licenciment","nommer","évaluation","évaluer, estimer","demandeur, requérant"]

En2 = ["manpower","take on","downsize","lay off","give notice","dismiss","dismissed"
       ,"dismissal","appoint","appraisal","appaise","applicant"]

Fr3 = ["demande, requête","évaluer","évaluation,analyse","démissionner","signe, panneau","démissions"
       ,"mutation, muter","transférant / cédant","sélectionner","employer"]

En3 = ["application","asses","assessement","resign","sign","resignation"
       ,"transfer","transferring","shortlisting","employ"]

Fr4 = ["emploi","bulletin de paie","heures supplémentaires","avantages en nature","bénévole","avenant"
       ,"ci-dessous","respecter","avoir droit","lier, obliger","tenu,relié"]

En4 = ["employement","pay slip","overtime","perks","volunteer","amendment"
       ,"hereunder","abide by","be eligible","bind","bound"]

Fr5 = ["selon lequel, par lequel","graphique ci dessous","salaire","salarié","conscient de","attaché a , qui aime bien"
       ,"marié avec"]

En5 = ["whereby","whereunder","salary","salaried","aware of","fond of","married of"]

Fr6 = ["informaticien","assistant de direction","employé de bureau","cadre"
       ,"demandeur d'emploi","stagiaire","agent de sécurité","commercial","graphiste","CV"]

En6 = ["IT technician","personal assistant","clerk worker","executive"
       ,"job seeker","intern","security guard","saleperson","graphic designer","resume"]

Fr7 = ["agence d'interim","fournir une reference","pointer , badget","personne nommée"
       ,"nomination","pose sa candidature","appliqué","évalué","congé annuel","conngé maternité","congé maladie"]

En7 = ["temp agency","provide a reference","clock in/out","appointee"
       ,"appointement","apply","applied","assessed","annual leave","maternity leave","sick leave"]

Fr8 = ["congé familial","renoncer à","employé transférés","etre sur la liste de candidats","présélectionner quelque chose"
       ,"employeur","employé,salarié","période d'essai"]

En8 = ["family leave","resigned","transferrd","to be shortlisted","shortlist"
       ,"employer","employee","trial period"]

Fr9 = ["à plein temps","àtemps partiel","salaire horaire","augmentation,augmeneter"
       ,"avantages","à son compte","partie","un accord","prévu/approuvé","qui lie"]

En9 = ["full time","part time","hourly wage","raise","benefits"
       ,"freelance","party","agreement","agreed","binding"]

Fr10 = ["classeur,relieur","salaire,paie","qui a peur de","capble de","jaloux de"
        ,"accuser quelqu'un de","en (bois,verre)","fier de","certain de","qui en a assez de"]

En10 = ["binder","wage","affraid of","capable of","jalous of","accuse somebody of"
        ,"made of","proud of","sure of","tired of"]

En = [En1,En2,En3,En4,En5,En6,En7,En8,En9,En10]
Fr = [Fr1,Fr2,Fr3,Fr4,Fr5,Fr6,Fr7,Fr8,Fr9,Fr10]


def ajouterMot():
       mot = []
       while (len(mot)<=10):
              i = randint(0, 9)
              j = randint(0, len(En[i])-1)
              if (Fr[i][j],En[i][j]) not in mot:
                     mot.append((Fr[i][j],En[i][j]))
       return mot


continuer = "oui"
manche = 1
aReviser = []


while (continuer == "oui"):
       mot = []
       score = 0
       mot = ajouterMot()
       for i in range(0,10):
              print(mot[i][0]," ?")
              reponse = input()
              if (mot[i][1] != reponse):
                     print("la bonne réponse est : ", mot[i][1])
                     print("")
                     aReviser.append(mot[i])
              else:
                     print("bien joué ! \n")
                     score+=1
       print(score,"/",10*manche)
       manche+=1
       if score != 10 :
              print("vous devez reviser : ")
              for k in range(0,len(aReviser)):
                     print(aReviser[k][1] , " qui veux dire ", aReviser[k][0])
       continuer=input("voulez vous continuer ? (oui pour continuer) ")
