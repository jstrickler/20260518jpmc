class Dog:
    def bark(self):
        print("woof! woof!")
    
    def wag(self):
        print("wag wag wag wag wag")

d = Dog()
print(f"{dir(d) = }\n")

colors = ["red", "purple", "black"]
attributes = [name for name in dir(colors) if not name.startswith('_')]
print(f"PUBLIC attributes: {attributes}\n")

w = getattr(d, 'wag') # get attribute by name   # like d.wag, but using a string
w()
print(f"{type(w) = }")


for a in animals:
    if hasattr(a, "wag"):
        a.wag()
