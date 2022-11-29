

# Buffering meaning reading from a disk
# cache is storing an information about a website visited before and return it if calls again
# cookies is a way of allowing your information to save a person information on a browser

# RECURSSION
# def recurse():
#     print("I am recurssing")
#     recurse()
#
#
#     def fact(n):
#         if n <=1:
#             return 1
#         return n * fact(n-1)
#     print(fact(n-1))
import json

temp_file = open("tem.txt", mode="w")

print("being thankful", file=temp_file)

print("this is good", file=temp_file)
temp_file.close()

# printing the text file to the terminal
temp_file = open("tem.txt", mode="r")
print(temp_file, file=temp_file)

# iterating through text files
temp_file = open("tem.txt", mode="r" )
for line in temp_file.readlines():
    for word in line.split(" "):
        print(word)


# using the keyword    WITH
with open("tem.txt", mode="r") as temp_file:
    for line in temp_file.readlines():
        for word in line.split(" "):
            print(word)


with open("tem.txt", mode="+r") as temp_file:
    for line in temp_file.readlines():
        for word in line.split(" "):
            print(word)
