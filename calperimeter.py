class Circle:
    def parameterof(self,r):
        p = 2 * 3.14 * r
        a = 3.14 * r * r
class Rectangle:
    def paramters(self,l, b):
        p = 2 (l + b)
        a = l * b
class Triangle:
    def parameter(self,a,b,c):
        p = a + b + c
        a= 0.5 * a * b
class Shape:
        ob = Circle()
        ob1 = Rectangle()
        ob2 = Triangle()
r = int(input("eneter raduis"))
a = int(input("enter value"))
b = int(input("enter value"))
c = int(input("enter value"))
print(ob.parameterof())
print(ob1.parameters())
print(ob2.parameter())