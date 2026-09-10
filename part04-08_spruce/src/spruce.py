# Write your solution here


def spruce(num):
    print("a spruce!")
    char = "*"
    i = num
    while num > 0:
        print(((num - 1) * " ") + char)

        char += "**"
        num -= 1

    print(((i - 1) * " ") + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
