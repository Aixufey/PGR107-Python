# MRO = Method Resolution Order
class A:
    pass


class B(A):
    num = 10


class C(B, A):
    num = 20


class D(C, A):
    pass


# MRO checks the first positional Parent chain if we have the same attributes in all classes
x = D()

print(x.num)


print(D.mro()) # checks D -> C -> B -> A  - Python checks in BFS order