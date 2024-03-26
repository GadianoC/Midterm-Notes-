# property decorator:
# = allow us to acess methods as attributes

# object instance of class
# and class is :

class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        email = f'{self.first_name}{self.last_name}@email.com'

    @property #Property Decorator (allows us to access methods as attributes)
    def email(self):
        return f'{self.first_name}{self.last_name}@email.com'
    # @full_name.setter #Property Decorator
            
    # .split (is used for splitting white space in string)
               
s1 = Student(first_name= 'Christian', last_name= 'Gadiano')