from numpy import empty


def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")


def looking_for_key(box):
    for item in box:
        if item.is_a_box():
            looking_for_key(item)
        elif item.is_a_key():
            print("found the key!")


def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)
