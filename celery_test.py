__author__ = 'weigl'

from msmlworker import hello, add

print(hello())

while True:
    a = hello.delay()
    b = add.delay(1, 2)
    print(a.get(timeout=10))
    print(b.get(timeout=10))


