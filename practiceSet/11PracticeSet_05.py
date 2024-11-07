# Write a class Vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        # Return the scalar dot product instead of a Vector object
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementations
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)   # Vector addition
print(v1 * v2)   # Dot product (scalar)

print(v1 + v3)   # Vector addition
print(v1 * v3)   # Dot product (scalar)
