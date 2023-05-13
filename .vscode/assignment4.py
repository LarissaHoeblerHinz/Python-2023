# 1 length of a string

length = str(input("say any word -> "))
print(len(length))

# 2 repetition

repeat = str(input("let's repeat this -> "))
repeat_ = repeat * 3
print(repeat_)

# 3 comparison

string1 = str(input("first word -> "))
string2 = str(input("second word -> "))
if string1 == string2:
    print("Is ", string1, " equal to ", string2, "? Result: True")
else:
    print("Is ", string1, " equal to", string2, "? Result: False")

# 4 longest word

sentence = str(input("say any sentence: "))
longest_word = max(sentence.split(), key=len)
print(longest_word, "-", len(longest_word))

# 5 replacement

ice = str(input("what do you think about icebear? "))
ice_assesment = ice.replace("bad", "good").replace("not", "")
print(ice_assesment)

# 9 password

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
