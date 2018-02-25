'''A list rotation consists of taking the last element and moving it to the front. For instance, if we rotate the list [1,2,3,4,5], we get [5,1,2,3,4]. If we rotate it again, we get [4,5,1,2,3].

Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k rotations. If k is not positive, your function should return l unchanged. Note that your function should not change l itself, and should return the rotated list.'''


def rotatelist(l, k):
    nl = l[:]
    if k <= 0:
        return l
    while k > 0:
        nl = nl[-1:] + nl[:-1]
        k = k - 1
    return nl


print(rotatelist([1, 2, 3, 4, 5], 1))
print(rotatelist([1, 2, 3, 4, 5], 3))
print(rotatelist([1, 2, 3, 4, 5], 12))
