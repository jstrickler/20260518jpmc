import inspect

def spam(p1: int, p2: str='a', *p3, p4: float, p5: str='b', **p6) -> None:  # define a function
    print(p1, p2, p3, p4, p5, p6)

# get argument specifications for a function
print("Function spec for Ham:", inspect.getfullargspec(spam))
print()
