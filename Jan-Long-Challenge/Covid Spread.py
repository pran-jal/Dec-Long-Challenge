T = int(input())
while T:
    N, D = map(int, input().split(' '))
    if D>21:
        print(N)
    else:
        if D<11:
            A = 2**D
            if N>A:
                print(A)
            else:
                print(N)

        else:
            A = 1024*3**(D-10)
            if N>A:
                print(A)
            else:
                print(N)
    T-=1
