#!/usr/bin/env python3

import random
import re

print()
dpool = ''
while dpool not in ['quit','q']:
    print("Enter your dice roll (ex. 2d6+1d4) or 'q' to quit:")
    dpool = input().lower()
    print()

    if dpool not in ['quit','q']:
        dice = re.findall(r'\d+d\d+', dpool)

        rolls = []
        for die in dice:
            val = die.split("d")
            numDice = int(val[0])
            valDice = int(val[1])

            for r in range(numDice):
                roll = random.randint(1,valDice)
                rolls.append(roll)
            
        print("Dice Rolled:", dpool)
        print("Result(s):", rolls)
        print("Sum:", sum(rolls))
        print()
exit