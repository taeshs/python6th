i = 1
i += 1


def myfun():
    b = i + 1
    print("myfunction i =", b)


myfun()

a = 50


def show():
    a = 10
    print("show-A: ", a)


show()
print("A:", a)


def show2():
    global a
    print("show2-A: ", a)
    a = 20
    print("show2-A: ", a)


show2()
print("A: ", a)
