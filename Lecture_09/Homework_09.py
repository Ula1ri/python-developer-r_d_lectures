n = int(input('go-go '))


def fibanacci(n):
    f1 = 1
    f2 = 1

    for __ in range(n):
        yield f1
        f1, f2 = f2, f1 + f2


f3 = list(fibanacci(n))

print(f3[-1])