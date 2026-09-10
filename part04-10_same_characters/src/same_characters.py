# Write your solution here


def same_chars(string, int1, int2):
    length = len(string) - 1

    if int1 > length or int2 > length:
        return False
    if string[int1] == string[int2]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(same_chars("cooler", 1, 9))
