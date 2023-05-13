even_num = []
odd_num = []


def find_number(numbers_list):
    for num in numbers_list:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)

    min_even = min(even_num)
    max_even = max(even_num)
    min_odd = min(odd_num)
    max_odd = max(odd_num)

    print(min_even)
    print(max_even)
    print(min_odd)
    print(max_odd)


# providing a list and calling the function
num_list = [45, 34, 12, 49, 40, 50, 51, 3, 4, 100, 101]
find_number(num_list)
