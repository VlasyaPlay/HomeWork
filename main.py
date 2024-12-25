# 1st program
print(9**0.5 * 5)


# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)


# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2) == (2 * (2 + 2)))


# 4th program
num_str = '123.456'
num_float = float(num_str)
shifted = num_float * 10
first_after_dot = int(shifted) % 10
print(first_after_dot)