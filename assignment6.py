# Task 1 – Scope and Namespace


def calculate_price():
    price = 10
    quantity = 5

    def apply_discount():
        discount = 0.1
        global price
        price = 10 * (1 - discount)
        total_price = price * quantity
        print("The total price including discount is", total_price, "$")

    apply_discount()


calculate_price()
# Variables defined within a local scope are limited to the scope of the function whereas global variables have a global scope and are not defined inside any function.

# Task 2 – Decorators
import time
from functools import wraps


def timeit(func):
    # decorater notes start time and end time after execution of function and thereby calculates the time difference
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@timeit
def example(num):
    total = sum((x for x in range(0, num**2)))
    return total


if __name__ == "__main__":
    example(10)
    example(100)
    example(1000)
    example(5000)
    example(10000)

# Task 3 – Best Practices

number_list = [1, 2, 3, 4, 5, 6, 7, 8]
total = 0
for number in number_list:
    # only numbers that can be divided by 2 - even numbers - should be part of the total sum
    if not number % 2:
        total += number
total

print("The sum of all even numbers in number_list is", total)
