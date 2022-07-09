petition = set()
answer = 0

while (answer != 3):
    print("\n----------------------------------")
    print("\t1. Add a name to the petition")
    print("\t2. See list of names")
    print("\t3. Quit")
    answer = int(input("> "))

    if (answer == 1):
        #Add name
        new_name = input("Enter a new name:\n")
        petition.add(new_name.lower())

    if (answer == 2):
        #Display petition
        count = 1
        for name in petition:
            print(f"{count}. {name.lower()}")
            count += 1
