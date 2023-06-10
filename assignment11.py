# task 1
# defining calculator as the outer function


def calculator():
    # operator is the inner function with two numbers as input that will be used in the mathematic operation
    def operator(a, b):
        return a + b

    return operator


closure = calculator()
# running the operation for different set of numbers
print(closure(1, 6))
print(closure(2, 3))

# task 2
import time
from functools import wraps


def timer(func):
    # decorater notes start time and end time after execution of function and thereby calculates the time difference
    @wraps(func)
    def timer_wrapper(a, b):
        start_time = time.perf_counter()
        result = func(a, b)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{a, b} took {total_time:.4f} seconds")
        return result

    return timer_wrapper


# definition of mathematical operation of which the execution time should be measured
@timer
def operation(a, b):
    sum = a * b
    return sum


if __name__ == "__main__":
    operation(10, 20)
    operation(50000, 400000)


# task 3
# creation of class rectangle with height and width as arguments
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # string method to "write out" the given arguments
    def __str__(self):
        return f"Rectangle: {self.height} times {self.width}"

    # equality comparison method to compare area of all defined rectangles
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.height * self.width == other.height * other.width

        return False


first = Rectangle(4, 5)
second = Rectangle(3, 5)
third = Rectangle(2, 10)

# printing results from string method
print(str(first))
print(str(second))
print(str(third))
# printing results from equality comparison method
print(first == second)
print(first == third)
