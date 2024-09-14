import random

# Generating a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random Integer: {random_int}")

# Genrating a random floating-point number between o and 1
random_float = random.random()
print(f"Random Float: {random_float}")

# Shuffling a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Shuffle List: {my_list}")

# Picking a random element from a list
colors = ['Red', 'Blue', 'Green', 'Yellow']
random_color = random.choice(colors)
print(f"Random Color: {random_color}")

# Generating a random sample of 2 elements from the list
sample_colors = random.sample(colors, 2)
print(f"Random Sample: {sample_colors}")