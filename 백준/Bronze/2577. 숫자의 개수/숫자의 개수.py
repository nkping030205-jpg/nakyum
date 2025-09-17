A = int(input())
B = int(input())
C = int(input())
result = A * B * C
result = str(result)
result = list(result)
a = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
for i in a:
    print(result.count(i))