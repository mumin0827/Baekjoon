import sys

input = sys.stdin.readline

M = int(input())
p = 1000000007
factorial = [1] * 4000001

for i in range(2, 4000001):
    factorial[i] = (factorial[i - 1] * i) % p


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p


for _ in range(M):
    N, R = map(int, input().split())

    print(factorial[N] * square(factorial[R] * (factorial[N - R]), p - 2) % p)