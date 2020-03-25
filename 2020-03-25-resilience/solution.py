T = int(input())

def resilience(d: int) -> float:

    return 0

for _ in range(T):

    a, b = map(int, input().split(' '))
    q = a/b
    for i in range(2, 9999999):
        r = resilience(i)
        if r < q:
            print(i)
            break
