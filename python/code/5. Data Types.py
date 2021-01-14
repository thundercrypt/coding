# Let's define some variables and do some experimentation with Data Types in Python.

num = 2.5
print(type(num))
# The output should be '<class 'float'>'.

num = 5
print(type(num))
# The output should be '<class 'int'>'.

num = 6+9j
print(type(num))
# The output should be '<class 'complex'>'.

a = 5.6
b = int(a)
print(type(b))
# The ouput should be '<class 'int'>'.

print(b)
# The output should be '5'.

k = float(b)
print(k)
# The output should be '5.0'.

k = 6
c = complex(b,k)
print(c)
# The output should be '(5+6j)'.

b<k
# The output should be 'True'.

comp = b < k
print(type(comp))
# The output should be '<class 'bool'>'.

b > k
# The output should be 'False'.

print(int(True))
# The output should be '1'.

int(False)
# The output should be '0'.

listOne = [25,36,45,12]
print(type(listOne))
# The output should be '<class 'list'>'.

s = {25,36,45,15,12,25}
print(s)
{36, 12, 45, 15, 25}
print(type(s))
# The output should be '<class 'set'>'.

t = (25,36,4,57,12)
print(type(t))
# The output should be '<class 'tuple'>'.

st = 'Random Text'
type(st)
# The output should be '<class 'str'>'.

ranch = range(10)
print(type(ranch))
# The output should be '<class 'range'>'.

print(list(ranch))
# The output should be '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'.

print(list(range(2,10,2)))
# This changes a range from 2 to 10 (10 exclusive) with an increment of 2.
# The output should be '[2, 4, 6, 8]'.

dictionary = {'Sushma':'English','Ritika':'Coding','Shivani':'Maths'}
# Sorry Ma'am, but writing the word 'Ma'am' was messing up the dictionary.
print(dictionary)
# The output should be '{'navin': 'samsung', 'rahul': 'Iphone', 'kiran': 'Oneplus'}'.
dictionary.keys()
# The output should be 'dict_keys(['navin', 'rahul', 'kiran'])'.
dictionary.values()
# The output should be 'dict_values(['samsung', 'Iphone', 'Oneplus'])'.
dictionary['Ritika']
# The output should be ''Iphone''.
dictionary.get('Coding')
# The output should be ''Oneplus''.
