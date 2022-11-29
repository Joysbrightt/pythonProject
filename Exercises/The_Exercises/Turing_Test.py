
# prompt user to enter what their problem is
# after the user enter input, ignore the response and ask what the problem is again
# if the user acknowledges to have encounter the problem before with(either yes or no)
# if the userinput is "yes", print you have it again.
# if the userinput is "no", print you have it now.

user_input = input("What is your problem?:\n ")

user_second_input = input("Have you had this problem before?\n ")
if user_input == "yes" or user_input == "Yes":
    print("Well, you have it again ")
elif user_input == "no" or user_input == "No":
    print("Well you have it now")
else:
    print("sorry it's not Tomi's problem")