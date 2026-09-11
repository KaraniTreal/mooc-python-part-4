# Write your solution here

my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))

    if index == -1:
        break

    num = int(input("New value: "))

    my_list[index] = num

    print(my_list)
