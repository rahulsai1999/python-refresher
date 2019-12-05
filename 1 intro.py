import sys

# variables and constants
x = 2
y = 3
z = x+y

# command line arguments
cli_a = sys.argv
print(cli_a[0])

# operations
print(3+4)
print(5-3)
print(4*5)
print(44/11)
print(48 % 12)
print(2**5)

# formatting output(int,float,exponential)
print("%2d, %5.2f" % (1, 05.333))
print("%3d, %2d" % (240, 120))
print("% 10.3E" % (356.08977))

# string operators
print(3 * 'un' + 'ium')

# lists
x = [1, 2, 3]
x.append(4)
x.pop()
x.pop(2)
print(x[1:])

if 2 in x:
    print("exists")

# dictionary
d = {'key1': 'item1', 'key2': 'item2'}
print(d['key1'])
print(d.keys())
print(d.values())
print(d.items())

# tuple
t = (1, 2, 3)
print(t[0])

# set - no repeated elements
s = {1, 2, 3, 1, 2, 3, 1, 3, 4, 2}
print(s)
