# song about cats
word = "cats"
for num in range(10, 0, -1):
    print(num, word, "in the room.")
    print(num, "dancing " + word + ".")
    print("Catch one cat.")
    print("Throw it out of the room.")
    if num == 1:
        print("No more dancing cats in the room.")
    else:
        new_num = num - 1
        if new_num == 1:
            word = "cat"
        print(new_num, word, "in the room.")
        print(new_num, "dancing " + word + ".")
    print()
print()

# song about many dogs
word2 = "angry dogs"
for num2 in range(0, 11, +1):

    if num2 == 0:
        print("No", word2, "in the room so far.")
    elif num2 == 1:
        word3 = "angry dog"
        print(num2, word3, "in the room.")
    else:
        print(num2, word2, "in the room.")
    print()