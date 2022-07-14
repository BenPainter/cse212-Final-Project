# Trees
Back to [Main](0-welcome.md)
## Introduction
Trees are linked links but with a twist. Instead of having one element in front and behind it, it has one before and many elements after it. For this tutorial, we will be going over binary trees, which contain two child elements, one on the right and one on the left. A tree will start with one element and as you progress up the level on the tree, more and more elements will be there. 

<img src="TreeDisplay.png" alt="Tree" width="500"/>


## How To Use A Tree
*The following will show how it is done in python, however, the concepts are the same for any language.

Since python does not have either Trees or Linked Lists in the base language, we will have to make it all by hand. There will be code examples in this section since all the functions will have to be created by the user.

Insert - The insert function allows the user to add a new element to the tree. Depending on how the tree is set up, the element will have to travel down a branch of the tree until it has found an empty spot to be stored.

Remove - The remove function allows the user to remove an element from the tree. In order to find the element, you have to climb up the branches until you reach the element that you were wanting to remove.


Contains - The contain function allows the user to search for an element in the tree. This function returns a boolean based on whether or not the element was found.

Traverse_forward/Backwards - The traverse_forward/backward function allows the returns of each element from the tree. Traveling forward through the tree will return the elements starting from the root level and traveling upwards through the tree. Traveling backward will start at the leaves and start heading downwards towards the root.

Height - The height function returns height from the longest branch in the tree. It must travel every branch to find the longest one.

Size - The size function returns how many elements are in the tree. This is usually stored inside the tree’s class.

Empty - The empty function returns a boolean based on whether or not the tree is empty. 

## Why To Use A Tree
### Pros
Sorts when inputted

### Cons
Doesn't keep track of history
could be imbalance

## Examples
Civ/Family Tree look up

## Efficiency
*\*These efficiencies are the average efficiency for these functions if the tree is well balanced. If the tree is all on one branch, then some of these functions will be more inefficient.*

The insert, remove, and contains functions each have an efficiency of O(log n). The reason for this is that they will only have to travel down one specific branch to achieve their task. 

The traverse_forward, traverse_backwards, and height functions each have the efficiency of O(n). The reason for it being O(n) is because you are visiting every single element in the tree no matter what. The number of elements will directly impact how long it will take. 

The size and empty functions have an efficiency of O(1). Size is usually stored in the class for the tree, so it is very easy to access. Empty has to check if the root of the tree is an element. It is also very cheap in processing, so it is O(1).


## Efficiency Chart
![Efficiency Chart](TreeEffciency.PNG)

## Try It Yourself


Here is a [template]() to start off from.

Once you are done with the problem, check with the [solution]().

