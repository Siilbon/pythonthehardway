class Animal(object):
    def __init__(self): #this is what is required on init
        self.traits = {'eyes' : 2, 'legs' : 4} #since these are for all animals they don't need to be in the __init__()
        self.teeth = 50

## Dog is a animal and has an name


class Dog(Animal):
    def __init__(self, name):
        ##A dog has a name
        Animal.__init__(self)
        self.name = name

## Cat is a Animal
class Cat(Animal):
    def __init__(self, name):
        ## A cat has a name
        Animal.__init__(self)
        self.name = name

## Person is an object
class Person(object):
    def __init__(self, name):
        ## A person has a name
        self.name = name

        ## person has a pet of some kind
        self.pet = None

## An employee is a person
class Employee(Person): 

    def __init__(self, name, salary):
        
        super(Employee, self).__init__(name)

        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass


rover = Dog("Rover")
rover.traits['eyes'] = 1 #poor rover only one eye

satan = Cat("Satan")
satan.traits['legs'] = 3 #poor satan, only 3 legs

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()


print "Rover has these traits\n" rover.traits
print "Satan has these traits" + satan.traits