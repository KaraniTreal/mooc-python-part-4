# Write your solution here

def everything_reversed(my_list):
   return [word[::-1] for word in my_list[::-1]]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]

    print(everything_reversed(my_list))

    
        