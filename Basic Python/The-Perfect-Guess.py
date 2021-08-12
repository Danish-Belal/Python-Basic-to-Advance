import random

Num = random.randint(1, 100)
print(Num)
userGues = None
Guesses = 0
while(userGues != Num):
    userGuess = int(input("Guess the Number\n"))
    if Num == userGuess:
        print("Congraculation! You Guess the correct Number 😀")
        break

    elif Num > userGuess:
        print("Guess Higher number Please 🙂")

    else:
        print("Guess Lower Number Please 🙃")
        Guesses += 1

print(f"You Guess the correct number in {Guesses} Guesses.")

# For Maintaning A High score Book. Using file.

with open('Highscoreforpractic-2.txt', 'r') as f:
    highscore = int(f.read())

if Guesses < highscore:
    with open('Highscoreforpractic-2.txt', 'w') as f:
        f.write(str(Guesses))










