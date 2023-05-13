pw = str(input("enter new password -> "))
pw_mod = pw.strip()
if (
    len(pw_mod) >= 8
    and any("a" <= c <= "z" for c in pw_mod)
    and any("A" <= c <= "Z" for c in pw_mod)
    and any(c.isdigit() for c in pw_mod)
):
    print("Well, well, well! Hello")
else:
    print("Please change your password according to the requirements mentioned below.")


if __name__ == "__main__":
    start_washing()

total = 0
for number in get_even_numbers:
    total += number
print("The sum of even numbers from 2 to 50 is", total)


def get_even_numbers():
    result = []
    # Only appending even numbers to list
    for number in range(1, 50):
        if number % 2 == 0:
            result.append(number)
    return result


print(get_even_numbers())
