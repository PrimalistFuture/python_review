# Slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

piano_keys[2:5]  # ["c", "d", "e"]
piano_keys[2:]  # ["c", "d", "e", "f", "g"]
piano_keys[:3]  # ["a", "b", "c"]
piano_keys[2:5:2]  # ["c", "e"]
piano_keys[::2]  # ["a", "c", "e", "g"]
piano_keys[::-1]  # ["g", "f", "e", "d", "c", "b", "a"]

# Class Inheritance


class Animal:
    """Animal"""

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        """Breathe"""
        print("Inhale, Exhale")


class Fish(Animal):
    """Fish"""

    def __init__(self):
        super().__init__()

    def swim(self):
        """Swim"""
        print("moving in water.")

    def breathe(self):
        """Does everything that Animal.breathe does, with some extra"""
        super().breathe()
        print("doing this underwater")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)  # still has access to this
print(nemo.breathe())
