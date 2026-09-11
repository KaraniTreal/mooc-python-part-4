# Write your solution here

my_list = []

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":
        if len(my_list) == 0:
            my_list.append(1)
        else:
            previous_num = my_list[-1]
            my_list.append(previous_num + 1)

    elif choice == "r":
        my_list.pop()

    elif choice == "x":
        break

print("Bye!")
