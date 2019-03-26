t = int(input())

for i in range(t):
    inp = input()
    a, b, n = inp.split(" ")
    a, b, n = int(a), int(b), int(n)
    bob_turn = n//2
    alice_turn = n - n//2

    a = a * (2 ** alice_turn)
    b = b * (2 ** bob_turn)

    if a > b:
        max_ = a
        min_ = b
    else:
        max_ = b
        min_ = a

    print(str(max_//min_))
