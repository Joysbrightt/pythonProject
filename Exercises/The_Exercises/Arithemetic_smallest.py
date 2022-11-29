

# write a script that input three integers
# display the sum, average, product, smallest and largest of those varible
# reimplement your script with a loop that input four integers

#
# user_input1 =int(input("Enter the first integer: "))
# user_input2 = int(input("Enter the second integer: "))
# user_input3 = int(input("Enter the third integer: "))
#
# user_input_sum = user_input1 + user_input2 + user_input3
# average = user_input_sum / 3
# product = user_input_sum * 3
#
# smallest = user_input3
# if user_input1 < smallest:
#     print("userinput1 is the smallest", user_input1)
# elif user_input2 < smallest:
#     print("userinput2 is the smallest ", user_input2)
# else:
#     print("userinput3 is the smallest ", user_input3)
#
#
# largest = user_input3
# if user_input1 > largest:
#     print("userinput1 is the largest", user_input1)
# elif user_input2 > largest:
#     print("userinput1 is the largest", user_input2)
# else:
#     print("userinput1 is the largest", user_input3)
#
# print(user_input_sum)
# print(average)
# print(product)


number = 0

while number <= 5:
    number = int(input("Enter an integer: "))
    number += 1
    sum = number + 1
    average = number / 3
    product = number * 3

    smallest = number

    if number < smallest:
        print("userinput1 is the smallest", number)
    elif number < smallest:
        print("userinput2 is the smallest ", number)
    elif number < smallest:
        print("userinput2 is the smallest ", number)
    else:
        print("userinput3 is the smallest ", number)

    largest = number
    if number > largest:
        print("userinput1 is the largest", number)
    elif number > largest:
        print("userinput1 is the largest", number)

    elif number > largest:
        print("userinput1 is the largest", number)
    else:
        print("userinput1 is the largest", number)

