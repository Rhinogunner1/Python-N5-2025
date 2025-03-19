
list = []
while True:
    test_score = int(input("Enter test score"))
    while test_score <0 or test_score> 100:
        print("Error, % must be between o and 100")
        test_score = int(input("Please enter a valid test_score "))

    list.append (test_score)
    print(list)