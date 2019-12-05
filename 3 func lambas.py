def my_func(x, y, z=5):
    return x+y+z


print(my_func(3, 4, 2))
print(my_func(1, 3))


def sq2(x): return x**2


print(sq2(5))

# map function

seq = [1, 2, 3, 4, 5]
print(list(map(sq2, seq)))
print(list(map(lambda x: x*2, seq)))

print(list(filter(lambda x: x % 2 == 0, seq)))
