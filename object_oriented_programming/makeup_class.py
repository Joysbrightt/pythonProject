


def func2(lst):
    counter = {}
    for item in lst:
        if(item in counter):
            counter[item] += 1


def func1(lst):
    from collections import defaultdict
    counter = defaultdict(int)

    for l in lst:
        counter[l] +=1

        return[k for k, _ in sorted(counter.items(), key= lambda x: x[1], reverse=True)]