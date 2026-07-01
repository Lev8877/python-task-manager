gen_squares = (number**2 for number in range(1,6))

print(next(gen_squares))
print(next(gen_squares))
print(list(gen_squares))
