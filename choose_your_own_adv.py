name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on dirt road, it has come to an end and you can go left or right. Type where do you want to go left or right?: ")

if answer == "left":
    answer = input("You come to river, you can walk around the river or swim across it. Type walk or swim: ")
    if answer == "walk":
        print("You walked many miles, ran out of water and lost the game.")
    elif answer == "swim":
        print("You swam across the river and were eaten by alligator.")
    else:
        print("It is not a valid answer!")

elif answer == "right":
    answer = input(
        "You come to the bridge it's look wobbly do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and drive a car.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet with some stranges, do you want to talk with them. (Yes/No)? ")
        if answer == "Yes":
            print("You talk to strangers and they give you gold. You WON!")
        elif answer == "No":
            print("You ignore the strangers and they kill you. You LOSS!")
        else:
            print("It is not a valid answer!")
    else:
        print("It is not a valid answer!")
else:
    print("It is not a valid answer!")

print("Thanks you for trying!", name)