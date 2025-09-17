N1 = int(input())
N2 = int(input())
N3 = int(input())
N4 = int(input())
N5 = int(input())
N6 = int(input())
N7 = int(input())
N8 = int(input())
N9 = int(input())

T = [N1, N2, N3, N4, N5, N6, N7, N8, N9]
A = [N1, N2, N3, N4, N5, N6, N7, N8, N9]

T.sort()
B = T[-1]
print(B)
print(A.index(B)+1)