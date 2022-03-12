# cook your dish here
T = int(input())
while T:
    N = int(input())
    if N&1 :
        print(N//2+1)
    else:
        print(N//2)
    T-=1
