import math

number = input("25 ")

try:
    float_number = float(number)
    rounded_number = math.ceil(float_number)
    print(rounded_number)
except ValueError:
    print("ไม่ใช่หมายเลขที่ถูกต้อง.")
