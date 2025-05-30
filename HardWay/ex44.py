#inheritance
'''class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass
'''
'''
class Parent(object):
    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")
'''
class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


#composition
class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class AChild(object):
    def __init__(self):
        self.other = Other()

    def override(self):
        print("ACHILD override()")

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("ACHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


dad = Parent()
son = Child()

'''
dad.implicit()
son.implicit()
'''
'''
dad.override()
son.override()
'''
dad.altered()
son.altered()

daughter = AChild()
daughter.implicit()
daughter.override()
daughter.altered()