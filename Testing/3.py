answer = input("Enter your answer (A-D): ")
while answer < "A" or answer > "D":
    print("Error. Invalid answer. Try again.")
    answer = input("Enter your answer (A-D): ")
print("You answered ",answer)