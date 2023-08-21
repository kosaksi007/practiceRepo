"""
Consider an array of non-negative integers, A second array is formed,
by shuffling the elements of the first array and deleting a random ele,
Find the missing ele in second array.

"""


def eleFinder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        print(num1, num2)
        if num1 != num2:
            return num1
    else:
        return arr1[-1]


num = eleFinder([1, 2, 3, 4, 5, 6, 6, 78, 99, 4, 20], [1, 2, 3, 4, 5, 6, 78, 99, 4, 20])
print(num)
