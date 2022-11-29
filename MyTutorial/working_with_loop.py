# # lst = ["Lagos", "Ogun", "Kwara", "Oyo", "Ibadan"]
# # print(lst[1::2])
# import math
#
# d = "eat"
# e = "eating"
# # print(d + e)
#
#
# # todo write words of at least 10 examples and make a copy of each
# #  todo and each word slice them with 2 steps
# # todo in each words perform a loop and print out each character
# # todo in each of the words print out the second character of the character
#
# the_list = ["food", "stuff", "make", "hello", "able", "enabling", "data", "python", "Java", "Javascript"]
# for tt in the_list:
#     # the_list =[:]
#
#     bt = "striethererhelkdfkladfalkdfdklfahd"
#
#     print(tt)


# # for a in the_list:
# #     print(a)
# #     for b in a:
# #         print(b)
# # print(f"The {the_list[1]} is hot")
# # print(f"The {the_list[0]} {the_list[1]}, can make one {the_list[4]} to practice {the_list[9]}")
# print(f"{the_list[0]}" + f"{the_list[1]}")
# print(the_list[0] + the_list[1])
#
# # a = the_list[:]
# # print(a)
# # print(the_list[1::2], the_list[4::4], the_list[6::9])
# # print(the_list[0][1:2])
#
#
# # todo take a number of thousands and millions and change it to an integers styles
# # todo make a list of 5 different entities and make copies of each of them in two different ways
# # todo make a 5 list of numbers and use loop to add the element in the list
# #  todo and use math functions to manipulate the list
# # todo add to list together and exponential operation and perform abs operation on them
# # todo do integer operation like reminders on them, addition...
#
#
# thelst = ['I', 'merit', 'ads', 'felt', 'fund']
# # de = ['I', 'merit', 'ads', 'felt', 'fund']
# # ty = ['I', 'merit', 'ads', 'felt', 'fund']
# # gh = ['I', 'merit', 'ads', 'felt', 'fund']
# # th = ['I', 'merit', 'ads', 'felt', 'fund']
# # ph = ['I', 'merit', 'ads', 'felt', 'fund']
#
# jsa = thelst[:]
# print(jsa)
#
# javaa = thelst
# print(javaa)
#
# mathe = [1, 2, 3, 4, 5]
# for a in mathe:
#     mathe =+ a
#     print(mathe)
#
# be= -121.45
# abs(be)
# print(abs(be))
#
# ba = 133
# bb =12
# print(ba/bb)
#
# bc = 8312121212.232
# print(f"the value of bc is {bc:.2f}")

def area(r):
    return 3.142 * r ** 2


# print(area(15))

def gradepoint(score):
    if score > 70-90:
        print(f"your {score} is and your gradepoint is A")
    elif score < 70:
        print(f"your {score} is and your gradepoint is B")
    elif score < 60:
        print(f"your {score} is and your gradepoint is C")
    elif score < 50:
        print(f"your {score} is and your gradepoint is 50")
    elif score < 40:
        print("you failed")


gradepoint(80)
