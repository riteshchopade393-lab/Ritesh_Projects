import random

'''
1  -> Snake
-1 -> Water
0  -> Gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ").lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw!")
elif (computer - you) in [-1, 2]:
    print("You win!")
else:
    print("You lose!")
