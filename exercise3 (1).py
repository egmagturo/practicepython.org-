#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


import random

randomlist = []
newlist = []

for i in range(0,10):
    n = random.randint(0,21)
    randomlist.append(n)

print('Initial list: ')
print(randomlist)

for element in randomlist:
    if element < 5:
        newlist.append(element)
        print(element)

print('list of elements <  5')
print(newlist)    


newnum = input('give me a number: ')
for element in randomlist:
    if element < int(newnum):
        newlist.append(element)

print(newlist)


# In[ ]:




