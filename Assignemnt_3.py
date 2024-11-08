s = 'fullstackslp'
# Use indexing to print out the following:  'f'
#1.1) 
print(s[0])  
# Use indexing to print out the following:  'p'
#1.2) 
print(s[-1])  
# Use indexing to print out the following:   'stack':
#1.3)
print(s[4:9])  
# Use indexing to print out the following:  'slp':
#1.4)
print(s[-3:])  
# Use indexing to print out the following:  'cks':
#1.5)
print(s[7:10])  
#Use indexing to reverse the string:
#1.6) 
print(s[::-1])  







#Problem 2 
#Using keys and indexing, grab 'hello' from the following dictionaries:
#2.1)
d1 = {'simple_key':'hello'}
print(d1['simple_key'])  
#2.2)
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])  
#2.3)
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])  

 #       Problem 3 
#Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique_values = set(mylist)
print(unique_values) 
 #                 Problem 4
#You are given the variables:
age = 45
name = "Kyle"
print(f"Hello my dog's name is {name} and he looks {age} years old")

