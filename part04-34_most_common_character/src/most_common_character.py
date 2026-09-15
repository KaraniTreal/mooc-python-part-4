# Write your solution here

def most_common_character(my_string):

    most_common = my_string[0]
    highest_count = my_string.count(most_common)

    for ch in my_string:
        current_common = my_string.count(ch)

        if current_common > highest_count:
            highest_count = current_common

            most_common = ch

    return most_common

if __name__ == "__main__":
    print(most_common_character("abcdbde"))
    print(most_common_character("exemplaryelementary"))




        



    



        