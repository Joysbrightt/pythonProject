def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low - high)
        guess = lst(mid)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            return None


def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile != 0:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")


# Todo
# using recursion algorithm to solve a problem

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


def solve_math(numb):
    numb = lambda x: x * numb


#     todo writing a factorial function

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def __main__():
    print(factorial(5))


# todo NESTED LIST

region = ["lagos", "ogun", "osun"], ["edo", "imo", "delta" "Anambra"], ["Kano", "Kaduna", "Jos", "Jigawa"]

