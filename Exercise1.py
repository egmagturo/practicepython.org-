#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


name  = input('What is  your name? ')
age = input('What is your age? ')
year =  2020 + 100 - int(age)
msg = 'Hello '+ name + '! You are ' + age + ' now. ' + 'On ' + str(year) + ', you will be 100 years old.\n'
print(msg)

num = input('Give me a number: ')
print(msg*int(num))


# In[ ]:





# In[ ]:




