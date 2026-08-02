# a, b, c (bitta qatorda)
# a va b ikkalasi ham juft bo'lsa True yoki c==0 bo'lsa True.
# result = (a%2==0 and b%2==0) or (c==0)
# True/False chiqaring.
a, b, c = map(int, input().split())
print((a % 2 == 0 and b % 2 == 0) or (c == 0))