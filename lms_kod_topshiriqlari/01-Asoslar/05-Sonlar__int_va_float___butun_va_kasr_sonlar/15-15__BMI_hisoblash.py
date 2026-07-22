# 1-qator: vazn (kg, float)
# 2-qator: bo'y (metr, float)
# BMI = vazn / (bo'y * bo'y)
# "BMI: <natija>" ko'rinishida chiqaring.
vazn = float(input())
boy = float(input())
bmi = vazn / (boy * boy)
print("BMI:", round (bmi, 1))