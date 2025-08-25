output = ""
star_rating = int(input("Enter star rating (0-5): "))
while star_rating < 0 or star_rating > 5:
    print("Error. Invalid rating. Try again.")
    star_rating = int(input("Enter star rating (0-5): "))
for index in range(0,star_rating):
    output = output + "*"
print(output)