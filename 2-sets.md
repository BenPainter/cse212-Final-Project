# Sets
Back to [Main](0-welcome.md)
## Introduction
A set is a simple data structure that has the unique attribute of not allowing any duplicated items in its collection. You are able to access any element at any time, however, the order that they entered the set is not stored. Sets use a technique called hashing to store each element, which in return, allows the user of a set to be able to remove, add, and if elements inside a set with very little cost.

## How To Use A Set
*The following will show how it is done in python, however, the concepts are the same for any language.

Since Python has sets already built into the language, we can use that when you want to create a set. The way to create a set variable is by creating a new variable and setting it to a set.
```python
New_set = set()
```

Add - The add command allows a user to try and input a new element to the set. You can try to add any element, but only non-duplicated items will actually be added. In Python, the add command looks like this.
```python
new_set.add(value)
```

Remove - The remove command allows the user to remove an element from the set. If the set does not contain what the user is trying to remove, it will throw an error.  In Python, the remove command looks like this.
```python
new_set.remove(value)
```
Member - The member command allows the user to search for an element in the set. This command returns a boolean based on whether or not the element is in the set. Python does not have a stand-alone function for this, so in order to use the member command, it would look like this.
```python
if value in new_set:
```
Size - The size command returns the total number of elements in the set. Python does not have a different function for size, so you can use the length command to achieve the same goal. 
```python
size = len(new_set)
```
## Why To Use A Set
### Pros
The greatest strength that sets have is their ability to prevent any duplicates from being stored in the set. Since sets use hashing, it also makes it very efficient when you need to add or remove elements from it. 

### Cons
One major downside to a set is that it does not keep track of order at all. There is no way to keep track of what element came first in the set.

## Examples
When some people want to create change, they will start a petition. A petition usually consists of a list full of people’s names. You aren’t allowed to have the same person same multiple times to inflate the numbers. Sets can help prevent that issue.

```python
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
```



## Efficiency
Since Set uses hashing to help store its data, it makes the command functions, such as adding and removing O(1). Searching through the set for an element as well as finding the size of the set is also O(1) because of the unique attributes of hashing.

## Efficiency Chart
![Efficiency Chart](SetEffciency.PNG)

## Try It Yourself
The youth are always coming up with new terms and lingo that will baffle even the wisest of scholars. Mr. Smith wants to be able to stay up to date with what his students are saying. He wants a program to allow his students to create a list of new terms that they use. Each student won’t know what the other students have submitted and Mr. Smith does not want to have the same term appear multiple times. Create a program to fulfill Mr. Smith’s request.

Here is a [template](2.2SETstudent_dictionary_problem.py) to start off from.

Once you are done with the problem, check with the [solution](2.2SETstudent_dictionary_solution.py).

