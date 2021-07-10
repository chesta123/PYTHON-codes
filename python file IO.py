# FILE IO BASICS
"""
r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string.
b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include images, documents, or all other files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file.
"""

# f = open('poems.txt','r')
# t= f.read()
# if "twinkle" in t:
#     print("yes twinkle is present")
# else:
#     print("twinkle is absent")
# f.close()
#
#
#
# def game():
#     return 656575
# score = game()
# with open("highscore.txt") as f:
#     hiscore = f.read()
# if hiscore== "" :
#     with open("highscore.txt","w") as f:
#         f.write(str(score))
# else:
#     if int(hiscore)<score:
#         with open("highscore.txt","w") as f:
#             f.write(str(score))






for i in range (2,21):
    with open(f"tables/multiplication_table_of_{i}", "w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j} \n")
    break


