#modules used in tip calculator program

import math

def truncate(amount,n):
    return math.floor(amount * 10 ** n) / 10 ** n

def fifteenPercent(billAmount):
    n = 2
    fifteenPercent = 0.15
    tip = billAmount * fifteenPercent
    total = billAmount + tip

    print("\n15%% tip = $", truncate(tip,n))
    print("new total = $", truncate(total,n))


def eighteenPercent(billAmount):
    n = 2
    eighteenPercent = 0.18
    tip = billAmount * eighteenPercent
    total = billAmount + eighteenPercent

    print("\n18%% tip = $", truncate(tip,n))
    print("new total = $", truncate(total,n))


def twentyPercent(billAmount):
    n = 2
    twentyPercent = 0.20
    tip = billAmount * twentyPercent
    total = billAmount + tip

    print("\n20%% tip = $", truncate(tip,n))
    print("new total = $", truncate(total,n))

