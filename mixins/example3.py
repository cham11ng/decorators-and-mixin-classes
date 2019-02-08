class A:
    def __init__(self):
        print('Initialize A')


class B(A):
    def __init__(self):
        A.__init__(self)
        print('Initialize B')


class C(A):
    def __init__(self):
        A.__init__(self)
        print('Initialize C')


class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('Initialize D')


if __name__ == '__main__':
    test = D()
