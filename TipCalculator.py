#Author: Phong Vang
#Date: 11.08.2018
#This program calculates a tip for 15%, 18%, and 20% of an input amount.

import Percentages

def main():

    print("Welcome to Tip Calculator program.")
    print("This program calculates the tip for a given amount.")

    billAmount = eval( input ("\nEnter an amount: $"));

    Percentages.fifteenPercent(billAmount)
    Percentages.eighteenPercent(billAmount)
    Percentages.twentyPercent(billAmount)


    print("\n\nHappy Tipping. End of Program.")

main()
