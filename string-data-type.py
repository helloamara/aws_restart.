# Exercice 1 : Présentation du type de données string
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
# Exercice 2 : Utiliser la concaténation des chaînes
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
# Exercice 3 : Utiliser des chaînes d'entrée
name = input("What is your name? ")
print(name)
# Exercice 4 : Formater des chaînes de sortie
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
