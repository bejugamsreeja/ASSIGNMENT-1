#!/usr/bin/env python
# coding: utf-8

# In[1]:


## write a python program to count the number of even and odd numbers from a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
             count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)



# In[2]:


## write a python program that accepts a word from the user and reverse it
w=input()
w1=""
for i in range(len(w)-1,-1,-1):
    w1=w1+w[i]
print(w1)


# In[3]:


## write a python program to get the Fibonacci series between 0 to 50
a,b=0,1
while b < 50:
    print(b,end=" ")
    a,b=b,a+b


# In[6]:


## write a python program to get the Fibonacci series between 0 to 50


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1



        

