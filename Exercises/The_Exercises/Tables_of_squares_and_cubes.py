

# write a script to calculate the squares and cubes of the numbers from 0 to 5
#  then print the resulting values in table format
# reimplement your script using a for loop and f-string

number =0
print("Number    Square     Cube")
while number <=9:
    number += 1

    print(f"{number}          {number *number}          {number * number * number}")