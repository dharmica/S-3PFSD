class Base:
    def display(self):
        print("Base class")


class Derived(Base):
    def display(self):
        print("Derived  class")


obj = Derived()
obj.display()