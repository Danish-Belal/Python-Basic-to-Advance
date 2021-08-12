# Gun , Snack and Water  Game.

import random

def gameWin(comp, you):
    if comp == you:
        return None
    if comp == 'S':
        if you == 'G':
            return True
        elif you == 'W':
            return False
    if comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True
    if comp == 'G':
        if you == 'W':
            return True
        elif you == 'S':
            return False


print("Computer Turn:  Snack(S) , Water(W) , Gun(G)")
randNo = random.randint(1, 3)
if randNo == '1':
    comp = 'S'
elif randNo == '2':
    comp = 'W'
else:
    comp = 'G'

you = input("Your Turn : Enter your choice , Snack(S) , Water(W) , Gun(G)? ")

a = gameWin(comp, you)

print(f"Computer Choice {comp}")
print(f"Your choice {you}")


if a:
    print("Congraculation! You Win")
elif a == None:
    print("Game is Tie")
else:
    print("Sorry! You lose")




