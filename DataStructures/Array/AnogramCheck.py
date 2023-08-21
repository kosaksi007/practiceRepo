# check the two arrays are anagram or not
def anagramChecker(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    arr1 = sorted(arr1.strip().upper())
    arr2 = sorted(arr2.strip().upper())
    if arr1 == arr2:
        return True
    else:
        return False


# out = anagramChecker('Dog', 'GoD')

def anagramChecker2(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    arr1 = arr1.strip().upper()
    arr2 = arr2.strip().upper()
    count = {}
    for ele in arr1:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1
    for ele in arr2:
        if ele in count:
            count[ele] -= 1
        else:
            count[ele] = 1
    for k in count:
        if count[k] != 0:
            return False

    return True


# out = anagramChecker2('Dog', 'GoD')
# print(out)
