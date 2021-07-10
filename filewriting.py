file1 = open('chesta','r')
print(file1.read())
print(file1.readline(6))
# readline character is used to print only one line of file.
print(file1.readline())
print(file1.readline())
file2 = open('smartfile','w')
file2.write("this thing will be printed in my smart file")
file2 = open('smartfile','a')
# a is for append i.e. to add something in file.
# run this code by commenting line 7 and 8 and using w instead of a in line 9
file2.write("this thing is added later on")
file2 = open('smartfile','w')

for things in file1:
    file2.write(things)
# this for loop is to copy everything from file chesta to file smartfile.
file2=open('smartfile','a')
file2.write("this is added afterwards")
