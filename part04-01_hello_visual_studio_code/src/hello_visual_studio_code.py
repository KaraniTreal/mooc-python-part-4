while True:
    editor = input("Editor: ")
    editor_lower = editor.lower()

    if editor_lower == "visual studio code":
        print("an excellent choice!")
        break

    elif editor_lower in ["word", "notepad"]:
        print("awful")

    else:
        print("not good")
