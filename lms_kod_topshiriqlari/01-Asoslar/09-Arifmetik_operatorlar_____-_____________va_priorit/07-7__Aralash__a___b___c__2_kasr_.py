# a, b, c (bitta qatorda)
# a + (b / c) ni hisoblang va 2 kasr bilan chiqaring.
# "Result: <natija>"
a, b, c = map(int, input().split())
print("Result:", f"{a + (b / c):.2f}")