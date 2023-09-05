#!/usr/bin/env python
# coding: utf-8

# # IRWA Lab 01

# ##### 1). Concatenate two lists index-wise

# In[1]:


teams = ["India", "England", "NZ", "Aus"]
captains = ["Kohli","Root","Williaamson", "Smith"]

zipped = zip(teams,captains)
zipped_list = list(zipped)
zipped_list


# In[2]:


teams = ["India", "England", "NZ", "Aus"]
captains = ["Kohli","Root","Williaamson", "Smith"]

zipped = zip(teams,captains)
zipped_dict = dict(zipped)
zipped_dict


# ##### 2) Given a list of books, their prices, and the quantities that you purchased, print out the total amount spent on each item

# In[3]:


books= ["textbooks", "exercise books", "story book", "drawing books"]
prices = [100,60,90,70]
quantities = [3,2,1,4]

for x,y,z in zip(books,prices,quantities):
    print(f"You bought {z} {x} for ${y * z}")


# ##### 3) Given a Python list. Add 10 to each item of the list 1

# In[8]:


List1 = [2,4,6,8,10]
x = [i+10 for i in List1]
print(x)


# In[7]:


List1 = [2,4,6,8,10]
List2 = []

for i in List1:
    i+=10
    List2.append(i)
    
print(List2)   
    


# ##### 4) Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order

# In[10]:


list1 = [10, 20, 30, 40]
list2 = ["Apples", "Mangoes", "Oranges", "Grapes"]

list2.reverse()

for x,y in zip(list1,list2):
    print(x,y)


# ##### 5) Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list

# In[28]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)

print(list1)


# ##### 6) Given a Python list, write a program to remove all occurrences of item 15.

# In[12]:


List1= [10,15,20,15,32,54,15]

while 15 in List1:
    List1.remove(15)

print(List1)


# ##### 7) Merge following two Python dictionaries into one

# In[13]:


dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
dict_2 = {'Bonnie': 18,'Rick': 20,'Matt': 16}

dict_1.update(dict_2)
print(dict_1)


# ##### 8) Change the key of the first entry from 0 to 4 in the following dictionary

# In[15]:


d = {0: 0, 1: 1, 2: 2, 3: 3}

k_old = 0
k_new = 4

d[k_new] = d.pop(k_old)
print(d)


# ##### 9) Theses two lists convert it into the dictionary

# In[16]:


country=["USA","France","India"]
capital= ["Washington D.C.","Paris","New Delhi"]

zipped = zip(country,capital)
zip_dict = dict(zipped)
print(zip_dict)


# ##### 10) Delete set of keys from Python Dictionary

# In[17]:


My_dict = {"Fruit": "Pear","Vegetable": "Carrot","Pet": "Cat","Book": "Moby dick","Crystal": "Amethyst"}

keysToRemove = ["Book", "Crystal"]

for i in keysToRemove:
    My_dict.pop(i)
    
print(My_dict)    


# ##### 11) Create a new dictionary by extracting the following keys from a given dictionary

# In[18]:


sub_dict = {'math' : 100, 'chem' : 98, 'sci' : 100,'eng':100}
key_to_extract = {'math', 'chem','sci'}

extracted_dic = {key:sub_dict[key] for key in sub_dict.keys() & key_to_extract}

print(extracted_dic)


# ##### 12) Given a list iterate it and display numbers which are divisible by 5.

# In[19]:


list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
list2 = []

for i in list1:
    if i in list1:
        if i % 5 == 0:
            list2.append(i)

print(list2)


# ##### 13) Write a program to display only those numbers from a list that satisfy the following conditions

# In[24]:


#• The number must be divisible by five
#• If the number is greater than 150, then skip it and move to the next number
#• If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break;
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)


# ##### 14) Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

# In[21]:


Substrings = "@W3Resource.Com"

def Count_chars(str):
    upper,lower,number,special = 0,0,0,0
    
    for i in range (len(str)):
        if str[i]>= 'A' and str[i] <= 'Z':
            upper +=1
        elif str[i] >= 'a' and str[i] <= 'z':
            lower +=1
        elif str[i] >= '0' and str[i] <= '9':
            number+=1
        else:
            special+=1
            
    return upper,lower,number,special
up,low,num,sp = Count_chars(Substrings)

print("upper case characters :", up)
print("lower case characters :", low)
print("numbers :", num)
print("Special characters :", sp)





# ##### 15) Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# In[23]:


n = 5
start = 2
seq = 0

for i in range(0,n):
    print(start, end = "+")
    seq += start
    
    start = start * 10+2
    
print("\no of series is " , seq)

