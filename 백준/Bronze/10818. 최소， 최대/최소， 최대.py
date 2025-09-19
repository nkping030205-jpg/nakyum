N = int(input())
A = input().split() # 이러면 리스트로 됨.
B = []
for i in range(0, N):
    B.append(int(A[i]))

B.sort()
print(B[0], B[N-1])