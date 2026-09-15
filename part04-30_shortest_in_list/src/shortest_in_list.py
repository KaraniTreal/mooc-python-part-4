# Write your solution here

def shortest(my_list):
    shortest_str = my_list[0]

    for word in my_list:
        if len(word) < len(shortest_str):
            shortest_str = word

    return shortest_str

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(shortest(my_list))
