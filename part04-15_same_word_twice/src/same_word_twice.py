# Write your solution here

words_list = []
while True:
    length = len(words_list)
    w = input("Word: ")

    if w in words_list:
        print(f"You typed in {length} different words")
        break

    words_list.append(w)
