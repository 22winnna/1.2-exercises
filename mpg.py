#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

choice = "y"
while choice.lower() == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost = float(input("Enter the cost per gallon:  "))


    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.") 
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost <= 0:
        print("Cost must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        tgs = round((gallons_used * cost), 2)
        cpm = round((cost * gallons_used / miles_driven), 1)
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:\t\t", tgs)
        print("Cost Per Mile:\t\t", cpm)

    choice = input("Get entries for another trip (y/n)? ")
    print()
print("Bye")



