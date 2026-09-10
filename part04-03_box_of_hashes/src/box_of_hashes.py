# Copy here code of line function from previous exercise


def line(num, string):
    if string == "":
        print(num * string)
    else:
        print(num * string[0])


def box_of_hashes(height):
    while height > 0:
        # You should call function line here with proper parameters
        line(10, "#")

        height -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
