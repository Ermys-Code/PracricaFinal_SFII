import random

print("Welcome to the Guess My Word App")

gameDict = {"Paises": ["españa", "portugal", "alemania", "francia", "italia", "inglaterra"], "Colores": ["rojo", "azul", "amarillo", "negro", "blanco", "verde"], "Dias": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"], "Asignaturas": ["matematicas", "historia", "ciencia", "ingles", "español", "fisica"]}

gameKeys= []
for key in gameDict.keys():
    gameKeys.append(key)

activeFlag = True

while activeFlag:
    gameCategoty = gameKeys[random.randint(0, 3)]
    gameWord = gameDict[gameCategoty][random.randint(0, 5)]
    
    blankWord = []
    for letter in gameWord:
        blankWord.append("-")

    print(f"\nGuess a {len(gameWord)} letter word form the following category: {gameCategoty.title()}")
    
    guess = ""
    guessCount = 0
    
    activeFlag2 = True
    while activeFlag2:
        print("".join(blankWord))
        guess = str(input("\nEnter your guess: "))
        guessCount += 1
        if guess == gameWord:
            print(f"Correct! You guessed the word in {guessCount} guesses.")
            activeFlag2 = False
        else:
            print("That is not correct. Let us reveal a letter to help you!")

            activeFlag3 = True
            while activeFlag3:
                letterIndex = random.randint(0, len(blankWord) - 1)
                if blankWord[letterIndex] == "-":
                    blankWord[letterIndex] = gameWord[letterIndex]
                    activeFlag3 = False

    try:
        f = open("./pf_sfii_data.txt", "a")
    except:
        f = open("./pf_sfii_data.txt", "w")
    f.write(f"1,{guessCount},\n")
    f.close()
    activeFlag = str(input("Would you like to play again (y/n): ")).lower() == "y"

totalWords = 0
totalTries = 0
line = ""
f=open("./pf_sfii_data.txt", "r")
with open('./pf_sfii_data.txt') as f:
    for line in f:
        linesList = line.split(",")
        totalWords += int(linesList[0])
        totalTries += int(linesList[1])
f.close()

print(f"\nYour total words are {totalWords} and your totat tries are {totalTries}")
print("\nThank you for playing our game.")