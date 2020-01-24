# Create a class for addition, subtraction, multiplication and division
class BasicMath:
    # Global Variables go first

    # Initialize with two variables (a, b)
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Addition
    def add(self):
        return self.a + self.b

    # Subtraction
    def sub(self):
        return self.a - self.b

    # Multiplication
    def mul(self):
        return self.a * self.b

    # Division
    def div(self):
        if self.b == 0:
            print('Cannot divide by 0!')
        else:
            return self.a / self.b

# Create another class raise the sum of A and B to the 'n' power or take the square root
class HarderMath(BasicMath):
    # Global Variables

    # Initialize the new variable 'n' using super function | give 'n' a default of n = 2
    def __init__(self, a, b, n = 2):
        self.n = n
        super().__init__(a, b) # Calls Parent

    # Exponentiation
    def expo(self):
        return (self.a + self.b) ** self.n

    # Take a square root
    def sqrt(self):
        if (self.a + self.b) > 0:
            print('Sum of A and B yields a negative number')
        else:
            return (self.a + self.b) ** 0.5

basicmath = BasicMath(1, 2)
hardmath = HarderMath(1, 2, 3)

def report():
    print(f'The sum of {basicmath.a} and {basicmath.b} is {basicmath.add()}')
    print(f'The difference of {basicmath.a} and {basicmath.b} is {basicmath.sub()}')
    print(f'The product of {basicmath.a} and {basicmath.b} is {basicmath.mul()}')
    print(f'The quotient of {basicmath.a} and {basicmath.b} is {basicmath.div()}')
    print(f'The power of {hardmath.a + hardmath.b} and {hardmath.n} is {hardmath.expo()}')
    print(f'The square root of {hardmath.a + hardmath.b} is {hardmath.sqrt()}')

if __name__ == "__main__":
    print(report())