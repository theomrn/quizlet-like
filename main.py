from random import *

Fr = ["douane","Réduire,réduction","reduire","reduction (en depense/personnel/production","quotidien","tableau de bord","jour de congés","date limite","affaire,marché,opération","traiter,s'occuper de,gerer,avoir"
      ,"Concessionnaire","concession","sans aucun doute","retard,retarder","charcuterie","ravi,heureux,enchanté","livrer,livraison","exiger,exigense","exigeant","retrograder"
      ,"cabosser,bosseler","nier","service (d'une entreprise)","deposer un depot (de l'argent)","meriter","ordinateur,PC","info,précisions,coordonnées","promoteur","composer,numéroter,cadran","agenda"
      ,"creuser","de la terre,saleté","handicapé, en panne","déçu","décvant","déception","reduction,remise","maladie","assiette,plat","licencier avec faute"
      ,"licenciement","expedier","a la disposition de","distraire","déranger","mettre un terme à,abolir","réduire (le nombre d'employer)","baisse","brouuillon,courrant d'air,rédiger","selectionner et deplacer,glisser-poser"
      ,"beaucoup","inconcénients","tiroir","retire (de l'argent)","dédiger,dresser","epouvantable,redoutable","permis de conduire","faire,laisser tomber","passer (par), venir,aller","deposer"
      ,"sécheresse","decharger","poussière","hollandais","tremblement de terre","reduire,detruire petit à petit","bord","efficassement","ascenseur","urgence"
      ,"emploi","permettre","ci-joint (dans une lettre)","occupé (la ligne,le tel)","améliorer","appreécier,aimer","demande de renseignements","s'inscrire,inscription","garantir","autorisé,avoir droit à"
      ,"bien que,même si","finalement","cadre (supérieur)","s'attendre à","attente","dépense","dépense,frais","cher","supplémentaire","tissu"
      ,"équipements,installation,service","usine","échouer,manquer de,ne pas (faire)","echec,ne pas (faire)","juste","de façon juste,plutôt,assez","automne,une chute","tomber,baisser","prendre du retard","échouer,tomber à l'eau"
      ,"tarif","la mode","robinet","peur","caractèristiquenspécialité,article de journal","mettre en vedette","frais","retour (d'info),réaction","aller chercher","domaine,champ"
      ,"chiffre","fichier,dossier,ranger en fiche,lime,limer,soumettre","meuble de classeur","compléter,remplir","se renseigner,découvir","amende,donner une amende","licencier ( avec faute)","de première heure"]

En = ["customs","cut","cut back/down","cutback","daily","dashboard","day off","dealine","deal","deal with"
      ,"dealer","dealershop","definitely","delay","delicatessen","delighted","deliver,delivery","demand","demanding","demote"
      ,"dent","deny","department","deposit","deserve","desktop","details","developer","dial","diary"
      ,"dig","dirt","disabled","disappointed","disappointing","disappointment","discount","disease","dish","dismiss"
      ,"dismissal","dispatch","disposal","distract","disturb","do away with","downsize","downturn","draft","drag and drop"
      ,"dramatically","drawback","drawer","draw out","draw up","dreadful","driving licence","drop","drop by","drop off"
      ,"drought","dump","dust","dutch","earthquake","eat away at","edge","efficiently","elevator","emergency"
      ,"employment","enable","enclosed","engaged","enhance","enjoy","enquiry,enquiries","enrol,enrolment","ensure","entitled"
      ,"even though","eventually","executive","expect","expectation","expenditure","expenses","expensive","extra","fabric"
      ,"facility","factory","fail","faillure","fair","fairly","fall","fall","fall behind with","fall through"
      ,"faire","fashion","faucet","fear","feature","feature","fee","feedback","fetch","field"
      ,"figure","file","filling cabinet","fill in/out","find out","fine","fire","first thing"]

def ajouterMot(En,Fr):
    mot = []
    while (len(mot) < len(En)):
        i = randint(0, len(En)-1)
        mot.append((En[i],Fr[i]))
        del En[i]
        del Fr[i]
    return mot

def test(En,Fr):
    """
    fonction test , demande tous les mots de la liste , s'ils sont connu les supprime ,
    pour arreter la boucle il faut soit connaitre tous les mots soit mettre -1 en reponse
    :param En: liste des mots en anglais
    :param Fr: liste des mots en fraçais
    :return: Ø
    """
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
            score += 1
            total += 1
            del mot[i]
            if (len(mot) == 0): break
    print("fin du programme")
    print("vous avez fais ", score, " / ", total)

def aleaMot(i,En,Fr):
    mot = []
    while (len(mot)<=i):
        k = randint(0,len(En)-1)
        if ([En[k],Fr[k]] not in mot):
            mot.append((En[k],Fr[k]))
    return mot

def apprendreImots(En,Fr):
    # liste initialiser a 0 , elle va servir a compter le nombre de fois qu'on mot a été connu
    print("pour stoper la boucle mettre -1")
    score = 0
    total = 0
    continuer = "oui"
    i = int(input("combien de mots voulez vous revisé ? \n"))
    mot = aleaMot(i, En, Fr)
    aReviser = [0 for i in range(len(mot))]
    while (continuer == "oui"):
        for j in range(0, i):
            alea = randint(0,len(mot)-1)
            print(mot[alea][1], " ?")
            reponse = input()
            if (mot[alea][0] != reponse):
                print("la bonne réponse est : ", mot[alea][0])
                print("")
                total += 1
            else:
                print("bien joué ! \n")
                aReviser[alea] += 1
                score += 1
                total += 1
                if (aReviser[alea] == 3):
                    del aReviser[alea]
                    del En[alea]
                    del Fr[alea]
                if (len(aReviser) == 0):
                    break
        continuer = input("voulez vous continuer ?\n")
    print("fin du programme")
    print("vous avez fais ", score, " / ", total)
    print("")
    if (len(aReviser) != 0):
        print("mot a reviser :")
        for i in range(0, len(aReviser)):
            print(En[i], " qui veux dire ", Fr[i])

def apprendre(En, Fr):
    """
    La fonction apprendre va faire passer les mots de toutes la listes , au bout de 3 fois ils sont supprimé
    :param En: liste des mots en anglais
    :param Fr: liste des mots en fraçais
    :return: Ø
    """
    aReviser = [0 for i in range(len(En))]
    # liste initialiser a 0 , elle va servir a compter le nombre de fois qu'on mot a été connu
    print("pour stoper la boucle mettre -1")
    reponse = ""
    score = 0
    total = 0
    continuer = "oui"
    while (continuer == "oui"):
        for j in range(0,10):
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
        continuer = input("voulez vous continuer ?\n")
    print("fin du programme")
    print("vous avez fais ",score," / ",total)
    print("")
    if(len(aReviser)!=0):
        print("mot a reviser :")
        for i in range(0,len(aReviser)):
            print(En[i]," qui veux dire ",Fr[i])


print("voulez vous apprendre ou faire un test ?")
rep = int(input("1 pour apprendre et 2 pour reviser ou 3 pour reviser une liste restrainte \n"))

if rep == 1:
    print("\n apprendre vous demande tous les mots vous devez avoir bon 3 fois de suite pour que le mot soit concidérer comme connu \n")
    apprendre(En,Fr)
if rep == 2:
    print("test vous donne tous les mots une fois et vous donne un score")
    test(En, Fr)
if rep == 3:
    print("\n apprendre vous demande i  mots vous devez avoir bon 3 fois de suite pour que le mot soit concidérer comme connu \n")
    apprendreImots(En,Fr)