T = int(input())
while T:
    T1, T2, R1, R2 = map(int, input().split(' '))
    if(T1/T2)**2 == (R1/R2)**3:
        print("Yes")
    else:
        print("No")
    T-=1
