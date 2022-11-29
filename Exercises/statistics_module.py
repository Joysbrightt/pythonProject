
# ZIP IS A BUILTIN FUNCTION
# zip take two or more iterable and combine them together
# ysefyl if one is working on two or more list together, it takes the smallest of all the iterable in the list given to it
# and return it and through it away



student_1 = [45,  67,98]
student_2 = [56, 78, 69]

print(list(zip(student_1, student_2)))
# comparing two student grade score list without one list longer than the other

student_3 = [45, 67,98]
student_4 = [56, 78, 69]
print(list((dict(zip(student_3, student_4)))))
# print((zip(student_1, student_2, strict=True)))
# having list of iterable and trying to wnat to make one a key

student_5 = [45, 67,98]
student_6 = [56, 78, 69]

print(dict(zip(student_5, student_6)))

# finding the maximum sconre for student in the list
s_scores = [max(subject) for subject in zip(student_5,student_6)]
student_slice = slice(1,3)
another_slicing_way = slice(1,3,4)
print("hello"[student_slice])
print("hello")
