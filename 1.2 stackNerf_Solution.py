magazine = []
answer = -1

def dart_type(num):
    if (num == 1):
        return "Standard"
    if (num == 2):
        return "Whistler"
    if (num == 3):
        return "Suction Cup"
    if (num == 4):
        return "Flat Head"
    else:
        return "Invalid number"

def load_dart(num_of_darts):
    if (num_of_darts >= 6):
        print("Your magazine is already full!")
        return
    else:
        print("\nDart Types:")
        print("1 - Standard")
        print("2 - Whistler")
        print("3 - Suction Cup")
        print("4 - Flat Head")
        dart_answer = int(input("> "))
        if(dart_answer , 4 and dart_answer > 1):
            magazine.append(dart_answer)
        else:
            print("Sorry, but that isn't a valid number")
def fire_dart():
    if (num_of_darts == 0):
        print("\nYour magazine is empty!")
        return
    else:
        print(f"You fired a {dart_type(magazine.pop())} dart")
        

while (answer != 0):
    num_of_darts = len(magazine)
    copy_magazine = magazine[:]
    print("\n***************************")
    if (num_of_darts != 0):
        print(f"A {dart_type(copy_magazine.pop())} dart is up next to fire")
    else:
        print("Your magazine is empty")

    print("\t0 - Quit")
    print("\t1 - load another dart")
    print("\t2 - fire the blaster")

    answer = int(input("> "))

    if (answer == 1):
        load_dart(num_of_darts)
    if (answer == 2):
        fire_dart()
