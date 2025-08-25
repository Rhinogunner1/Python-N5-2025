age = int(input("Enter your age: "))
while age < 0 or age >= 117:
    print("Error. Invalid age. Try again.")
    age = int(input("Enter your age: "))
print("Thank you. Your age has been recorded as",age)