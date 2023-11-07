import math

# 度分秒を十進数に変換する関数
def dms_to_decimal(degrees, minutes, seconds):
    return degrees + minutes / 60 + seconds / 3600

# 十進数での角度からサインを求める関数
def calculate_sine(decimal_degrees):
    # ラジアンに変換
    radians = math.radians(decimal_degrees)
    # サインを計算
    return math.sin(radians)

# ユーザーから度分秒の入力を受け取る
degrees = int(input("度を入力してください: "))
minutes = int(input("分を入力してください: "))
seconds = int(input("秒を入力してください: "))

# 度分秒を十進数に変換
decimal_degrees = dms_to_decimal(degrees, minutes, seconds)
print(f"十進数での角度: {decimal_degrees}")

# サインを計算
sine_value = calculate_sine(decimal_degrees)
print(f"サインθ: {sine_value}")