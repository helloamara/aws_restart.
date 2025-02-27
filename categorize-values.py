# Catégoriser les valeurs
#Exercice 1 : Créer une liste de types mixte
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))