"""
Given a string “S” containing a set of words,
transform it such that the words appear in the reverse order.
One or more spaces separate words in “S”.
"""


def converter(S: str):
    temp = S.split(" ")
    tempstr = ' '.join(temp[::-1])
    print(tempstr)


# converter("My name    us Khan")

"""
Given an unsorted set of numbers from 1 to N with exactly two missing numbers,
find those two missing numbers.
"""


def findMissing1(s: set):
    templist = list(s)
    templist.sort()
    missingList = []
    for ele in templist:
        i = templist.index(ele)
        if ele + 1 == templist[i + 1]:
            pass
        else:
            missingList.append(ele + 1)
            if len(missingList) == 2:
                break
    return missingList


def findMissing2(s: set):
    templist = list(s)
    for i in range(1, len(templist) + 2):
        if i not in templist:
            print(i)


"""
You are given an array of integers, arr, of size n, 
analogous to a continuous stream of integers input. 
Your task is to find “K” largest elements from a given stream of numbers.
"""


def lagestnums(arr: str, K: int):
    tempList = [int(x) for x in arr]
    tempList.sort()
    print(tempList[-K:])


# lagestnums("1234567890",3)

"""
Given an integer array arr of size n, find all magic triplets in it. 
A Magic triplet is a group of three numbers whose sum is zero.
"""


def find_magic(arr: list):
    triplets = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                n = int(arr[i]) + int(arr[j]) + int(arr[k])
                tempList = []
                if n == 0:
                    tempList.extend([int(arr[i]), int(arr[j]), int(arr[k])])

                if len(tempList) != 0:
                    triplets.append(tempList)
    for i in range(len(triplets)):
        for j in range(i + 1, len(triplets)):
            count = 0
            for ele in triplets[i]:
                if ele in triplets[j]:
                    count += 1
            if count == 3:
                del triplets[i]
    print(triplets)


# nums = [-1, 0, 1, 2, -1, -4]
# find_magic(nums)
"""
POP:
n = list_name.pop('index') --> returns the popped value. 
    aThe pop() function removes the last element or the element based on the index given.
Remove:
list_name.remove(element_value) 
    remove() function removes the first occurrence of the specified element
    Do not return anything
Delete:
del list_name['index'] or del list_name
    The del keyword removes the element specified by the index, 
    deletes the whole list as well as slices the list
    Do not return anything
    It requires the index value, or else it deletes the whole list.    
Insert:
    list_name.insert(index,value)
Extend:
    list_name.extend([value/values])
Append:
    list_name.append(value)
"""
listing = ['1', '-2', '2', '2']
# lis.insert(3, 1)
# print(lis)
# string = ",".join(listing)
# print(string)
for ele in listing:
    if ele.isalpha():
        print('yes!!!')
