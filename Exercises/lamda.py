
#
# lst = [1,2,3,4,5]
#
# for item in lst:
#     print(item, end= ' ')
#
#
#
#
#     # LIST COMPREHENSION
#
# lst = []
# for i in range(10):
#     lst.append(i)
# print(lst)
#
#
# # building list without using a for loop
#
# lst = [i for i in range(1,10)]
# print(lst)
#


# building list by collecting the data from user and saving it

#
# lst = [number:= int(input("Enter a number from one to ten: ")) for number in range(1,10) if number % 2 != 0 lst.append(number)]
# print(lst)

# using list to build through numbers
# lst = [i for i in range(1,10) if i % 2 != 0]
# print(lst)
#
#
# # using list to build through numbers
#
# lst = []
# for i in range(10):
#
#     if i % 2 !=0:
#         lst.append(i)
# print(lst)


# doing little exercise

lst = []
for i in range(65,91):
    lst.append(chr(i))
    print(lst)

    # list comprehension

    lst =[chr(i) for i in range(65,91)]
    print(lst)