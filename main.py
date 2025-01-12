class Cat:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   def walk(self):
      print("cat is walking")
   def make_sound(self):
      print("Meow")

class Dog:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   def walk(self):
      print("dog is walking")
   def make_sound(self):
      print("Bark")

dino =  Dog("Dino", 2)
milo =  Cat("Milo", 3)

for animal in (dino, milo):
   animal.make_sound()
   animal.walk()