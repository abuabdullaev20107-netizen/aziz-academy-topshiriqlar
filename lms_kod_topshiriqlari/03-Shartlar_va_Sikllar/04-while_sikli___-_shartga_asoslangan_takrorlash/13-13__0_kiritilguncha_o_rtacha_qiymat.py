x = int(input())
s = 0
count = 0
while x != 0:
    s += x
    count += 1
    x = int(input())
if count == 0:
    print(0)
else:
    print(s / count)