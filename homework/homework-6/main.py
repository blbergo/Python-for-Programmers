# lab 1
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        return f'Person(name={self.name}, birth_year={self.birth_year})'
    
class Student(Person):
    def __init__(self, name, birth_year, major):
        super().__init__(name, birth_year)
        self.major = major
    
    def __repr__(self):
        return f'Student(name={self.name}, birth_year={self.birth_year}, major={self.major})' 
    
class Instructor(Person):
    def __init__(self, name, birth_year, salary):
        super().__init__(name, birth_year)
        self.salary = salary
    
    def __repr__(self):
        return f'Instructor(name={self.name}, birth_year={self.birth_year}, salary={self.salary})'
    
# lab 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __repr__(self):
        return f'Employee(name={self.name}, salary={self.salary})'
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department
        
    def __repr__(self):
        return f'Manager(name={self.name}, salary={self.salary}, department={self._department})'
    
class Executive(Manager):
    def __init__(self, name, salary, department, bonus):
        super().__init__(name, salary, department)
        self._bonus = bonus
        
    def __repr__(self):
        return f'Executive(name={self.name}, salary={self.salary}, department={self._department}, bonus={self._bonus})'

def main():
    print("============= Lab 1 =================")
    # test the Person class
    p1 = Person("John", 1990)
    print(p1)
    
    # test the Student class
    s1 = Student("Alice", 2000, "CS")
    print(s1)
    
    # test the Instructor class
    i1 = Instructor("Bob", 1970, 50000)
    print(i1)
    
    print("\n============= Lab 2 =================")
    # test the Employee class
    e1 = Employee("John", 50000)
    print(e1)
    
    # test the Manager class
    m1 = Manager("Alice", 60000, "CS")
    print(m1)
    
    # test the Executive class
    ex1 = Executive("Bob", 70000, "CS", 10000)
    print(ex1)
    
    
if __name__ == "__main__":
    main()