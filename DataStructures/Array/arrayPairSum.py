"""
Given an integer array(list), output all the unique pairs that sum up to a specific value K
"""


def pairSum(arr: list, K: int):
    if len(arr) < 2:
        return print("False")
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tempSum = arr[i] + arr[j]
            if tempSum == K:
                pairs.append([arr[i], arr[j]])
    print(pairs)


# pairSum([1, 3, 2, 2], 4)
def pairSum2(arr: list, K: int):
    if len(arr) < 2:
        return print("False")
    output = []
    for num in arr:
        target = K - num
        arr.remove(num)
        if target in arr:
            output.append([num, target])
    print(output)


pairSum2([1, 3, 2, 2,2,4,5,63,2], 4)
