
# write a script that separate a five-digit integer
# display them


# number = int(input("Enter a five-digit integer: "))
# print(int(number / 10000 % 1000), end=' '), print(int(number % 10000 / 1000), end=' '), print(int(number / 100 % 10), end=' '), \
#
# print(int(number % 100 / 10), end=' '), print(int(number % 10), end=' ')
#

number = input("Enter a five-digit integer: ")

for number in number:
    print(number, end = ' ')