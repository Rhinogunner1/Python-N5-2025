
list = []
while True:
    name_of_user = (input("Enter Name here:"))
    age_of_user = int(input("Please enter an age for the talent show "))
    while age_of_user <11 or age_of_user> 18:
        print("Error, age must be between 11 and 18")
        age_of_user = int(input("Please enter a valid age "))
    if age_of_user >11 or age_of_user< 18:
        print("You are allowed to enter the talent show, hope you do well!")
    list.append (age_of_user)
    print(list)