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
    # Remember that the magazine size is only 6
    '''
    Your Code Here
    '''

def fire_dart():
    # Remember that you can't shoot an empty gun
    '''
    Your Code Here
    '''
        

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
