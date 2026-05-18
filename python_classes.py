    
class Person:
    # class data
    # constructor (initializer)  __init__()
    # instance methods
    # properties
    # class methods
    # static methods

    DEPARTMENTS = ['abc', 'def']

    def __init__(self, first_name, last_name):
        self._first_name = first_name  # "private" instance attribute
        self._last_name = last_name


    @property
    def dept1(self):
        return self.DEPARTMENTS[0]
    

    @property  # decorator
    def first_name(self):  # getter property (managed attribute)
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):  # setter property
        if isinstance(value, str):
            self._first_name = value
        else:
            raise TypeError(f"first name must be str, not {type(value).__name__}")
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str):
            self._last_name = value
        else:
            raise TypeError(f"last name must be str, not {type(value).__name__}")

    @property
    def last_name_upper(self):
        return self._last_name.upper()
    

    def doit(self):
        print("doing it")

    @staticmethod
    def double(value):
        return value * 2

if __name__ == "__main__":
    p1 = Person("John", "Doe")  #  __init__(self, "John", "Doe")
    print(f"{p1 = }")   # p1 = .....
    print(f"{p1.first_name = }")  # bad practice to access private attribute
    print(f"{p1.last_name = }")
    print(f"{p1.last_name_upper = }")
    print(f"{p1.last_name.upper() = }")
    p1.first_name = "Srini"
    print(f"{p1.first_name = }")
    try:
        p1.first_name = 123
    except TypeError as err:
        print(err)
    else:
        print(f"{p1.first_name = }")
        
    print(f"{p1.dept1 = }")
    print(f"{Person.DEPARTMENTS[0]} = ")
    p1.doit()
    print(f"{Person.double(5) = }")
    
    
    
