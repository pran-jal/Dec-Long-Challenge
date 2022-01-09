T = int(input())
while T:	
	N,K = map(int, input().split(' '))
	N = N-1
	for i in range(N+1):
	    if(2<<i)%N == 1:
	        count = i+1
	        break
	
	if count == K :
	    itr = N+1
	elif count > K:
	    itr = (1<<K)%N
	elif count < K:
	    itr = 1<<(K%count)%N
	    
	Z = 0
	for i in range(N+1):
	    print(Z+1, end=' ')
	    Z=(Z+itr)%N
	    if Z == 0:
	        Z = N
	        
	print()
	T-=1
