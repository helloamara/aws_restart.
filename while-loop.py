# Utiliser les boucles
import random
# Utiliser les boucles
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
# généreration d'un nombre aléatoire entre 1 et 10 en utilisant la fonction randint()
number = random.randint(1,10)
isGuessRight = False
# Pour gérer la logique du jeu, créez une boucle while
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
# Écrire la boucle for
for x in range (0, 11):
    print(x)
