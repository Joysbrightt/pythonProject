

lst = [num for num in range(1,11)]
evens = [num for num in  range(1,11) if num % 2 == 0]
even_and_square_odds = [num if num% 2 ==0 else num **2 for num in range(1,11)]
lst_input = [int(input("Enter a number: ")) for num in range(1,4)]

list_nested_for = [(x,y) for x in range(1,5) for y in range (6,10)]
upper_names = [name.upper()for name in ("Dolapo","Tolani", "Florence" )]
# upper_names = [upper(name) for name in ("Dolapo","Tolani", "Florence" )]

list_of_dicts = [{key: value} for key, value in zip(upper_names, evens)]




print(lst)
print(evens)
print(even_and_square_odds)
print(lst_input)
print(list_nested_for)
print(upper_names)
print(upper_names)
print(list_of_dicts)