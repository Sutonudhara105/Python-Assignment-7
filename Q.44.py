'''Write a program to merge two dictionaries.'''

dict1 = {'a':10, 'b':5, 'c':8, 'd':4, 'e':1}
dict2 = {'f':20, 'b':15, 'g':18, 'h':14, 'e':11}

dict3 = {**dict1, **dict2}
print("two dictionaries are\n")
print(dict1)
print(dict2)
print("sorted dict is\n")
print(dict3)
