stack = ["Bill","Eric","Jill","Rio","Ryle","Ivy","Jacob"]
answer = -1
print ("Welcome Back Mr. Smith")

while(answer != 0):
    remaining = len(stack)          # Length command
    print("\n******************************")
    print("\t0. Quit")
    print("\t1. Add a student")
    print("\t2. Grade latest paper\n")
    if (remaining != 0):            # Empty command
        print(f"Remaining papers to grade: {remaining}" )
    else:
        print("There are no more papers to grade.")
    answer = int(input("> "))

    if (answer == 1):
        new_student = input("\nThe name of the student:\n\t")
        stack.append(new_student)   # Push Command
    if (answer == 2):
        if (remaining != 0):
            student = stack.pop()   # Pop Command
            print(f"\nYou have graded {student}'s paper")
        else:
            print("\nYou can't grade anymore. You're done!")

