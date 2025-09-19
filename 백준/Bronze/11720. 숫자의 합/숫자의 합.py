N = int(input())
X = str(input())

Y = []
for i in range(0, N):
    Y.append(int(X[i]))

Z = 0
for i in range(0, N):
    Z += Y[i]

print(Z)