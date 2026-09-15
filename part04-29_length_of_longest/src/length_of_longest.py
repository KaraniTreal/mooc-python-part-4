# Write your solution here

def length_of_longest(my_list):
    longest = 0

    for word in my_list:
        if len(word) > longest:
            longest = len(word)

    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(length_of_longest(my_list))