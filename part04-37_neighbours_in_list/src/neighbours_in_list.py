# Write your solution here

def longest_series_of_neighbours(my_list):
    longest_streak = 1
    current_streak = 1

    for i in range(len(my_list) - 1):
        if abs(my_list[i] - my_list[i + 1]) == 1:
            current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak

        else:
            current_streak = 1

    return longest_streak

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
