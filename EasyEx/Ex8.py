class Person:
    name = "PTIT"

    def __init__(self, name = None):
        self.name = name

jeffrey = Person("Bang")
print ("%s name is %s" % (Person.name, jeffrey.name))
nico = Person()
nico.name = "Bang share to learn"
print ("%s name is %s" % (Person.name, nico.name))