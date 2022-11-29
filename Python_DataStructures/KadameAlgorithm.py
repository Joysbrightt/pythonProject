# Maximum sub array

lst = [-4, 2, -5, 1 - 2, 3, 6, -5, 1]

global_max = lst[0]
currents_max = lst[0]

for i in range(1, len(lst)):
    if currents_max < 0:
        currents_max = lst[i]
    else:
        currents_max += lst[i]

    if currents_max > global_max:
        global_max = currents_max

# print(global_max)

# Rearrange Sorted List.

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 2, 3, 4, 5]


def Rearrange_Sorted_List(lst1):
    start = 0
    end = len(lst1) - 1
    empty_list = []
    while start <= end:
        empty_list.append(lst1[end])
        empty_list.append(lst1[start])

        if len(empty_list) > len(lst1):
            empty_list.pop(-1)
    return empty_list



print(Rearrange_Sorted_List(x))
