# Write a class 'complex' to represent complex numbers, along with overloaded operators '+' and '*' which add and multiplies them


class Complex:
    def __init__(self, m,n):
        self.m = m
        self.n = n

    def __add__(self,c2):
        return Complex(self.m + c2.m, self.n + c2.n)
    
    def __mul__(self,c2):
        real_part = self.m * c2.m - self.n * c2.n
        imaginary_part = self.m * c2.n + self.n * c2.m
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.m} + {self.n}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)    
print(c1 * c2)
