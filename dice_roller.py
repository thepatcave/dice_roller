import random

print("Enter your dice roll (ex. 2d6):")
dice = input()
print()

val = dice.split("d")
numDice = int(val[0])
valDice = int(val[1])

rolls = []
for r in range(numDice):
    roll = random.randint(1,valDice)
    rolls.append(roll)
    
print("Dice Rolled:", dice)
print("Result(s):", rolls)
print()