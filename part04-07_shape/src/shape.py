# Copy here code of line function from previous exercise and use it in your solution


def line(num, string):
    print(num * string)


def shape(size, char1, heightr, char2):
    i = 1
    while i <= size:
        line(i, char1)
        i += 1

    j = 1
    while j <= heightr:
        line(size, char2)

        j += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
