if 1 < 2:
    print("Yep")
elif 3 > 2:
    print("Nope")
else:
    print("Nothing")

seq = [1, 2, 3, 4, 5]

for i in seq:
    print(i, end=" ")

for i in range(0, 14, 2):
    print(i, end=" ")

i = 1
while i < 5:
    print('i is {}'.format(i))
    i = i+1

# list comprehension
x = [i**2 for i in seq]