class Parrot:
    # attributes
    species = "bird"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # variables with underscore as a prefix
        self._actualName = "Psittaciformes"

    # member functions
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

    def setter(self, another):
        self._actualName = another


blu = Parrot("Blu", 12)
wes = Parrot("Wes", 15)

# access static attributes or class attributes
print(blu.__class__.species)

# access instance or object attributes
print(blu.name)
print(blu.age)

print(blu.sing("happy"))
print(blu.dance())

blu._actualName = "something else"
blu.setter("something")
print(blu._actualName)
