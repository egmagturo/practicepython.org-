#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

new = []
n = input('give me a number: ')

for i in range(1,int(n)+1):
    if int(n) % i == 0:
        new.append(i)
        print(i)

print(new)


# In[ ]:





# In[ ]:




