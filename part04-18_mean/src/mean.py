# Write your solution here


def mean(my_list: list):
    addition = sum(my_list)
    return addition / len(my_list)


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
