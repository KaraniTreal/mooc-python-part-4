# Write your solution here

num_items = int(input("How many items: "))

my_items = []

i = 1

while num_items > 0:
    item = int(input(f"item {i}: "))

    my_items.append(item)

    i += 1

    num_items -= 1

print(my_items)
