#Author: Phong Vang
#Date: 10.22.2015
#This program calculates a tip percentage for a given amount.

def main():

    print("Welcome to Tip Calculator program.")
    print("This program calculates a tip amount for any given amount.")

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
