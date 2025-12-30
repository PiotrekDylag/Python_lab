def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# for i in fib(9):
# print(i)

imiona = ["anna", "piotr", "andrzej"]
nowa = list(map(lambda x: x.capitalize(), imiona))
print(nowa)

oceny = [1, 2, 4, 2, 1, 6]
filtered = list(filter(lambda x: x>=4, oceny))
print(filtered)
