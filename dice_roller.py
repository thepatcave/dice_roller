#!/usr/bin/env python3

import random
import re

dPool = ''
while dPool not in ['quit','q']:
    print('\n' + 'Enter your dice roll (ex. 2d6+1d4) or \'q\' to quit:')
    dPool = input().lower()
    valid = re.search(r'\d+d\d+', dPool)

    if valid:
        dice = re.findall(r'\d+d\d+', dPool)

        print('\n' + 'Dice Rolled:' + ' {}'.format(dPool))
        print('\n' + 'Result(s):')

        tRolls = []
        for die in dice:
            val = die.split("d")
            numDice = int(val[0])
            valDice = int(val[1])

            rolls = []
            for r in range(numDice):
                roll = random.randint(1,valDice)
                rolls.append(roll)
            print("  {} = {}; Sum = {}".format(die, rolls, sum(rolls)))
            tRolls.append(sum(rolls))
            
        print('\n' + 'Total:' + ' {}'.format(sum(tRolls)))
        print()

print()
exit