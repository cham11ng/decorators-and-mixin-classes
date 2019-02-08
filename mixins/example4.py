class A:
    def __init__(self):
        print('Initialize A')


class B(A):
    def __init__(self):
        super().__init__()
        print('Initialize B')


class C(A):
    def __init__(self):
        super().__init__()
        print('Initialize C')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('Initialize D')


if __name__ == '__main__':
    test = D()
    print(D.__mro__)
