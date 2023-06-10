# task 1
# writing in the input.txt file
file_path = "input.txt"
with open(file_path, "w") as file:
    file.write("Hello, how is your day? Today is a beautiful day.")

# reading from input.txt
with open(file_path, "r") as file:
    content = file.read()
    print(content)


# creating definition for word _count, here for a regulat string
def word_count(str):
    counts = dict()
    words = str.split()

    # if there are several occurences, count them respectively, else it's only one occurence
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# text from file is given as an input
print(word_count(content))


# task 2
# creating the function with two arguments a and b
def sum_of_squares(a, b):
    # squares of a and b
    x = a**2
    y = b**2
    # sum of squares defined above
    mult = x + y
    return mult


# printing the results for two given numbers
print(sum_of_squares(5, 3))

# task 3
#
from statistics import mean


def calculate_average(*numbers):
    average = mean(numbers)
    return average


print(calculate_average(2, 10, 5, 3))
