# cook your dish here
T = int(input())
while T:
    S = input()
    a=-1
    N = len(S)
    s = S[0]
    e = S[N-1]
    
    i = 0
    while i < N-1:
        temp=0
        j = i+1
        while j < N-1 and (S[j]!=s and S[j]!=e):
            j+=1
            temp+=1
        if temp:
            a = max(a, temp)
        i=j
            
    print(a)
    T -=1
