def printfib(n):
    lis = []
    for i in range(n):
        def fibanocci(n: int):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibanocci(n - 1) + fibanocci(n - 2)

        x = fibanocci(i)
        lis.append(x)
    return lis


n = printfib(10)
print(n)


def fibanocci(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibanocci(n - 1) + fibanocci(n - 2)


for i in range(4):
    n = fibanocci(i)
    print(f'i = {i} -->', n)

