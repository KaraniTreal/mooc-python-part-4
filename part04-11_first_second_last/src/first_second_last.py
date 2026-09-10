# Write your solution here


def first_word(string):
    space1 = string.find(" ")
    return string[0:space1]


def second_word(string):
    space1 = string.find(" ")
    remaining_string = string[space1 + 1 :]
    space2 = remaining_string.find(" ")
    if space2 == -1:
        return remaining_string
    else:
        return remaining_string[0:space2]


def last_word(string):
    last_space = string.rfind(" ")
    return string[last_space + 1 :]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
