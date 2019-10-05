import math

def threeSumClosest(A, B):
    A = sorted(A)
    ans = math.inf
    final_sum = 0
    for i in range(0, len(A) - 2):
        first = A[i]

        a = i+1
        b = len(A) - 1
        while a < b:
            sum_ = first + A[a] + A[b]

            if abs(sum_ - B) < ans:
                ans = abs(sum_ - B)
                final_sum = sum_
            if sum_ < B:
                a += 1
            else:
                b -= 1

    print(final_sum)


threeSumClosest([-1, 2, 1, -4], 1)