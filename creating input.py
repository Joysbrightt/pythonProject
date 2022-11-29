# lst = ['a', 'b', 'c', 'd', 'e']
# lst = list("abcde")

lst = list("abcdefghijk")
lst += [1,2,3,3]
# print(' '.join(lst))
# print(lst[4])

# print(lst[1:5])
# print(lst[:: -1])
# print(lst [-4])
# print(lst * 2)
# print (lst)
# print (lst[:: 2])
# print ('a' in lst)
# print ('q' in lst)
# print ('q'not in lst)
#
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")
# print("Hello world!\nHello world!\nHello world!") #printing three times on a single line
# print(" Hello " + " Angela")
# print("Hello"+" "+ "Angela")

# list_of_lists =[1,2,[3,4,5],6]
# print(list_of_lists[2])
# print(list_of_lists)
#
# num = 5
# var = num if num % 2 ==0 else 3
# print(var)

my_dict = {
'name': "Seguan",
'age': 12,
'sex': 'MALE',
'hobby': ['Python', 'Java'],
'is_wife_beater': False}

# print(len(my_dict))
# print(my_dict)
#
# for key in my_dict:
#     print(key)
#     print(key, '-->', my_dict[key]) #looping through the key in my_dict
#
# # for key in my_dict.keys():
# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key,'-->', value)
# print(my_dict.items())
# #passing the dict constructor
#
# prof = dict(name = 'segun', age=12)
# print(prof)

# ls = ['segun', 'sege', 'oko', 'mama' 'e']
# # ls.append("kurubente", "kurubente", "koga", "ju","go", "lo")
# #extend and += does the same work
# ls.extend(["kurubente", "kurubente", "koga", "ju","go", "lo"])
# ls+= ("kurubente", "kurubente", "koga", "ju","go", "lo")
#
# print(ls)

fruits = ["apple", "banana", "cucumber", "pear"]
print(fruits)
# fruits.extend("orange")
# fruits.append("orange"
# fruits.extend(["orange", "stone"])

#tuple
fruits.extend(("orange", "stone"))
# fruits.insert(1, "grape")
# fruits.insert(-1, "grape")
fruits.insert(len(fruits), "grape")
# print(fruits.clear())
# print(fruits.pop())
# fruits.remove('apple')

print(fruits)
# print(fruits.index("cucumber", 3,))

fruits.sort()
# fruits.sort(key=len)
fruits.reverse()
print(fruits)