dictionary = set()
answer = 0


while (answer != 4):
    print("\n*******************")
    print("\t1. Add a word")
    print("\t2. Remove a word")
    print("\t3. Check list")
    print("\t4. Quit")
    answer = int(input("> "))

    if (answer == 1):
        #Add words
        new_word = input("Enter a new word:\n")
        dictionary.add(new_word.lower())

    if (answer == 2):
        #Remove words
        remove_word = input("What word would you like to remove:\n")
        remove_word = remove_word.lower()
        if remove_word in dictionary:
            dictionary.remove(remove_word)
        else:
            print("That word is not in the dictionary")


    if (answer == 3):
        #Display dictionary
        for word in dictionary:
            print(word)
