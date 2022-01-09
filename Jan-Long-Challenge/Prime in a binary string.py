T = int(input())
while T:
    S = input()
    for i in range(len(S)):
        if S[i] == '1' and i<len(S)-1:
            print("Yes")
            break;
    else:
        print("No")
    T-=1
