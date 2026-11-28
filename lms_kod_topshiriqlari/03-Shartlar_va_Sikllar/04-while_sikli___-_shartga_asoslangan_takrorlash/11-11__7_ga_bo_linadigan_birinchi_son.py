n = int(input())
i = 1
while i <= n and i % 7 != 0:
    i += 1
if i <= n:
    print(i)
else:
    print("No")