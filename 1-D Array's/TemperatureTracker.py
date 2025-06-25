#Create a program that allows a user to:
#Enter 5 daily temperatures between -20 and +50 C
#Display all temperatures
#Calculate and display the average temperature
#Your program should use input validation, a 1-D array and fixed loops.

temperatures = [] 
for index in range (0,7):
    temp = input("Enter a daily temperatures between - 20 and +50 C:")
    while temperatures <-20 or temperatures > 50:
            print (" These are invalid temperatures ")
            temp = int(input("Please re-enter valid temperatures"))
            temperatures.append(temp)

    
    