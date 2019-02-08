class A:
    def __init__(self):
        print('Initialize A')


class B(A):
    def __init__(self):
        A.__init__(self)
        print('Initialize B')


class C(B):
    def __init__(self):
        B.__init__(self)
        print('Initialize C')


if __name__ == '__main__':
    test = C()
