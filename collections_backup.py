# Lab Utiliser les listes, tuples et dictionnaires
# Exercice 1 : Présentation du type de données list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
# Pour accéder à la chaîne apple
print(myFruitList[0])
#Pour accéder à la chaîne banana
print(myFruitList[1])
print(myFruitList[2])
# Modification des valeurs dans une liste
myFruitList[2] = "orange"
print(myFruitList)
# Exercice 2 : Présentation du type de données tuple
# Créez un tuple en saisissant le code suivant :
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
# Exercice 3 : Présentation du type de données dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
# Accéder à un dictionnaire par nom
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
