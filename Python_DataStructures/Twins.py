x = [1, 2, 2, 3, 3]


def twinsAlgorithm():
    firstNumber = x[:]
    for i in x:
        findTwin = range()
        if i[:] == x[:]:
            return x[i]
        else:
            return -1

    # The correct snippet for TwinsAlgorithm
    for i in range(0, len(x), 2):
        if x[i] != x[i + 1]:
            return x[i]
        else:
            return -1

    if x[-1] != x[-2]:
        return x[-1]
