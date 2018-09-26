# song about cats
word = "cats"
for num in range(10, 0, -1):
    print(num, word, "in the room.")
    print(num, "dancing", word, ".")
    print("Catch one cat.")
    print("Throw it out of the room.")
    if num == 1:
        print("No more dancing cats in the room.")
    else:
        new_num = num - 1
        if new_num == 1:
            word = "cat"
        print(new_num, word, "in the room.")
        print(new_num, "dancing", word, ".")
    print()