from sys import stdout

def main():
    t = int(input())
    while t > 0:

        print("Q 0 0")
        stdout.flush()
        check = int(input())

        print("Q 0 " + str(check))
        stdout.flush()
        check2 = int(input())
    
        lrPoint = (2*check - check2)//2;
        print("Q 0 " + str(lrPoint))
        stdout.flush()

        check3 = int(input())

        xl = check3
        yl = check - check3

        print("Q 1000000000 1000000000")
        stdout.flush()

        check = int(input())

        print("Q 1000000000 " + str(yl))
        stdout.flush()

        check2 = int(input())

        xh = (1000000000 - check2)
        yh = (1000000000 - check + check2)

        print("A {} {} {} {}".format(xl, yl, xh, yh))
        stdout.flush()

        ans = int(input())
        t = t - 1;

        if ans > 0:
            continue
        else:
            break

# MAIN ---
main()