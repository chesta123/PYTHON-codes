def function1():
    print("oop sikhni h")
func2 = function1
del function1
func2()

def funcret(num):
    if num == 0:
        return print
    elif num ==1:
        return sum

print(funcret(1))


def qwerty(func):
    func("hulk")
qwerty(print)

def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

@dec1
def who_is_chesta():
    print("chesta is a dedicated girl to learn oop")
# who_is_chesta = dec1(who_is_chesta)
who_is_chesta()

@dec1
def gfgu():
    print("testing decorators")
gfgu()