import random

randno = random.randint(1,3)

print("Computer's turn")

if randno == 1:
    ct="snake"
elif randno == 2:
    ct="water"
else:
    ct="gun"


pi=input("Your turn: Snake{s} Water{w} or Gun{g}?")

# pt=str()

if pi==("s"):
    pt="snake"
elif pi==("w"):
    pt="water"
else:
    pt="gun"


print("You chose", pt)
print("Computer chose", ct)

if ct==("water"):
    if pt==("gun"):
        print("Computer won")
    elif pt==("snake"):
        print("You won")
    else:
        print("Tie")
elif ct==("snake"):
    if pt==("gun"):
        print("You won")
    elif pt==("water"):
        print("Computer won")
    else:
        print("Tie")
else:
    if pt==("gun"):
        print("Tie")
    elif pt==("snake"):
        print("Computer won")
    else:
        print("You won")