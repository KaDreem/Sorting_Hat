def hogwart():
    gryffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    slytherin = 0

    print("Answer with Y or N using only your subconcious:")
    answer = input("Are you brave? ")
    if answer == "Y":
        gryffindor += 1

    answer = input("Should loyalty come before the self? ")
    if answer == "Y":
        hufflepuff += 1

    answer = input("Are you full of yourself? ")
    if answer == "Y":
        ravenclaw += 1

    answer = input("Can you decieve others? ")
    if answer == "Y":
        slytherin += 1

    answer = input("Do you have a sense of adventure? ")
    if answer == "Y":
        gryffindor += 1

    answer = input("Are you a nerd? ")
    if answer == "Y":
        ravenclaw += 1

    answer = input("Are you an aspiring med school student? ")
    if answer == "Y":
        hufflepuff += 1

    answer = input("Do you prefer to work alone? ")
    if answer == "Y":
        slytherin += 1

    answer = input("Are you competitive? ")
    if answer == "Y":
        gryffindor += 1


    # Determine which house has the highest score and print the result
    if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
        print("You belong in Gryffindor!")
    elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
        print("You belong in Hufflepuff!")
    elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
        print("You belong in Ravenclaw!")
    elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
        print("You belong in Slytherin!")
    else:
        print("An error has occured, please contact administration to get your hold removed in order to register for classes.")
hogwart()