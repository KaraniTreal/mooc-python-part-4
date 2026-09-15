# Write your solution here

def all_the_longest(my_list):
    longest = []
    max_length = 0

    for word in my_list:
        if len(word) > max_length:
            max_length = len(word)

            longest = [word]

        elif max_length == len(word):
            longest.append(word)



    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result)