T=int(input())
while T :
    N,M=map(int, input().split())
    
    if N>M:
        t=''.join([''.join(['0','10'*(M+1)]),'010'*(N-M-1)])
    elif M>N:
        t=''.join([''.join(['1','01'*(N+1)]), '101'*(M-N-1)])
    elif M==N:
        t=''.join(['1', '01'*M, '0'])
    
    print(len(t),'\n'+t)
    T=T-1
