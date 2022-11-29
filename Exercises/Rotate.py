

def rotate(lst, k):
    k = k % len(lst)
    # a = [1,2,3,4,5,5,6,7]
    # a[-2:] +a [:-2]
    
    return lst[-k] +lst[:-k]


lst = []
for i in range [1,11]:
    lst.append(i)
    # lst(range(1,11))
    
    # list comprehension writing in one line

var = [i for i in range(1, 11)]