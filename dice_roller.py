import random

dice = ''
while dice not in ['quit','q']:
    print("Enter your dice roll (ex. 2d6):")
    dice = input().lower()
    print()

    if dice not in ['quit','q']:
        val = dice.split("d")
        numDice = int(val[0])
        valDice = int(val[1])

        rolls = []
        for r in range(numDice):
            roll = random.randint(1,valDice)
            rolls.append(roll)
            
        print("Dice Rolled:", dice)
        print("Result(s):", rolls)
        if numDice > 1:
            print("Sum:", sum(rolls))
        print()
exit