# Write your solution here

def no_vowels(string):
    new_string = ""
    vowels = "aeiouAEIOU"

    for ch in string:
        if ch not in vowels:
            new_string += ch

    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))