# Write your solution here


def list_of_stars(my_list: list):
    for n in my_list:
        print(n * "*")


if __name__ == "__main__":
    my_list = [2, 3, 4, 6]
    list_of_stars(my_list)
