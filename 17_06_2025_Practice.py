# 2929. Distribute Candies Among Children II

number_of_candies = 3
limit = 3

from itertools import product

elements = [0, 1, 2,3]

# Generate all combinations of length 3 with repetition
combinations = list(product(elements, repeat=3))
t = 0
# Print combinations
for combo in combinations:
    v = sum(combo)
    if v == number_of_candies:
        t+=1
        print(combo)

print(t)