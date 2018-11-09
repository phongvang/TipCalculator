#Author: Phong Vang
#Date: 11.08.2018
#This program calculates a tip for 15%, 18%, and 20% of an amount.

import Percentages

def main():

    print("Welcome to Tip Calculator program.")
    print("This program calculates the tip for a given amount.")

    billAmount = eval( input ("\nEnter an amount: $") );

    fifteenPercent = billAmount * .15
    totalBill1 = billAmount + fifteenPercent
            
    eighteenPercent = billAmount * .18
    totalBill2 = billAmount + eighteenPercent
                       
    twentyPercent = billAmount * .20
    totalBill3 = billAmount + twentyPercent

    print("\n(15% tip): $", fifteenPercent)
    print("The total is $%.2f" % (totalBill1))

    print("\n(20% tip): $",eighteenPercent)
    print("The total is $%.2f" % (totalBill2))

    print("\n(25% tip): $",twentyPercent)
    print("The total is $%.2f" % (totalBill3))

    print("\n\nThank you for using this program!")

main()
