# Write your solution here

def formatted(my_list):
    new_list = []

    for num in my_list:
        form = f"{num:.2f}"

        new_list.append(form)

    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    result = formatted(my_list)
    print(result)
    


