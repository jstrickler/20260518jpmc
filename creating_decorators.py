from datetime import datetime
from functools import wraps


def timestamp(original_function):

    @wraps(original_function)
    def _wrapper(*args, **kwargs):
        print(datetime.now())
        return original_function(*args, **kwargs)  # calls spam()
    return _wrapper

@timestamp
def spam():
    print("SPAM!")
# spam = mydeco(spam)

@timestamp
def ham(ham_count):
    print("HAM" * ham_count)


spam()
spam()
ham(3)
spam()
ham(8)

print(f"{spam.__name__ = }")
print(f"{ham.__name__ = }")

