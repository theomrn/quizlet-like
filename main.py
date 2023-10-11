from random import *

Fr1 = ["(taux de) présence du personnel","dédaigneux / condéscendant","éloge","évaluateur, expert","motivation","acceptant / contestant"
       ,"alors que , tandis que","par la présence","intérimaire","prestataire","poste vacant"]

En1 = ["Staff attendance","dismissive","praise","assersor","incentive","agreeing"
       ,"whereas","herby","temp","contractor","vacancy"]

Fr2 = ["main d'oeuvre, effectifs","embaucher","réduire les effectifs","licencier pour motif économique","donner son preavis","renvoyer","licencié"
       ,"licenciment","nommer","évaluation","évaluer, estimer","demandeur, requérant"]

En2 = ["manpower","take on","downsize","lay off","give notice","dismiss","dismissed"
       ,"dismissal","appoint","appraisal","appaise","applicant"]

Fr3 = ["demande, requête","évaluer","évaluation,analyse","démissionner","signe, panneau","démissions"
       ,"mutation, muter","transférant / cédant","sélectionner","employer"]

En3 = ["application","asses","assessment","resign","sign","resignation"
       ,"trasfer","transferring","shortlisting","employ"]

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
       ,"employer","employee","trial periode"]

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








continuer = "oui"

while (continuer == "oui"):
       for k in range(0,9):
              i = randint(0, 9)
              j = randint(0, len(En[i]))
              print(Fr[i][j], " ? ");
              reponse = input()
              if (En[i][j] != reponse):
                     print("la bonne réponse est : ", En[i][j])
              else:
                     print("bien joué ! ")
       continuer=input("voulez vous continuer ? (oui pour continuer) ")
