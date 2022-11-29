x = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
movement = len(x) - k
window = x[0: k]

window_sum = sum(x[0:k])
maximum = window_sum

for i in range(movement):
    window_sum = window_sum - x[i] + x[k]
    # print(window_sum)
    if window_sum > maximum:
        maximum = window_sum
    i+=1
    k+=1

print(maximum)


