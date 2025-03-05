#input 
lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
additionalRows = int(input("Please enter the number of additional rows included for free: "))
specialOffer = input("Is a special offer running? (y/n): ")

#Process
widthOfSquarePacks = lengthOfSquarePacks
if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
    totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
if specialOffer == "y":
    widthOfSquarePacks = widthOfSquarePacks + additionalRows

widthOfSquarePacks = lengthOfSquarePacks

#Output
print("The number of cans in the pack is: "+str(totalNumberOfCans))