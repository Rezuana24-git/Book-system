n=int(input())
result=0
for i in range(n):
    m=input()
    if "+" in m:
        result += 1
    elif "-" in m:
        result -= 1
print(result)
