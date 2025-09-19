N = int(input())
A = input().split() # 이러면 리스트로 됨.

B = []
D = []
# 리스트의 요소를 정수화 시켜서 큰 수대로 정렬을 시키자.
for i in range(0, N):
    B.append(int(A[i]))
    D.append(int(A[i]))

for i in range(0, (N-1)):
    for c in range(1, N):
        i < c
        if B[i] > B[c]:
            B[i] = D[c]
            B[c] = D[i]
        else:
            pass            

print(B[0], B[(N-1)])
