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

# 十進数での角度からサインを求める関数
def calculate_tan(decimal_degrees):
    # ラジアンに変換
    radians = math.radians(decimal_degrees)
    # サインを計算
    return math.tan(radians)

# 角度のリストを定義 (度、分、秒のタプルのリスト)
angles_dms = [
    # (6, 46, 0),
    # (6, 46, 30),
    # (13, 38, 30),
    # (13, 39, 30),
    # (20, 43, 00),
    # (20, 44, 00),
    (28, 8, 30),
    (28, 10, 00),
    (28, 8, 00),
    (28, 9, 30),
    # (36, 6, 30),
    # (36, 9, 30),
    # (36, 7, 00),
    # (36, 9, 30),
    # (44, 58, 30),
    # (45, 5, 00),
    # (45, 0, 00),
    # (45, 3, 30),
    # (55, 40, 00),
    # (55, 44, 30),
    # (55, 35, 30),
    # (55, 40, 30),
    # (69, 59, 30),
    # (70, 10, 30),
    # (70, 32, 00),qww
    # (70, 42, 30),
]

# 各角度の十進数とサインを計算し出力
for degrees, minutes, seconds in angles_dms:
    # 度分秒を十進数に変換
    decimal_degrees = dms_to_decimal(degrees, minutes, seconds)
    print(f"十進数での角度へ変換 ({degrees}度 {minutes}分 {seconds}秒)===> {decimal_degrees}")

    # サインを計算
    sine_value = calculate_sine(decimal_degrees)
    print(f"sinθ: {sine_value}")

    # lamda1 = sine_value*10000/2
    # print(f"lamda1: {lamda1}")


    # lamda2 = sine_value*10000/2/2
    # print(f"lamda2: {lamda2}")
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

    # m=3
    m=4
    # m=5
    # m=6
    # m=7
    # m=8 


    # ここの変数を、変えながら出力することに注意。
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

    lamdam = sine_value*10000/2/m
    print(f"lamdam: {lamdam}")

    # delta_lamda1 = 7.3/100000*lamda1/calculate_tan(decimal_degrees)
    # print(f"deltalamda2: {delta_lamda1}")

    # delta_lamda2 = 7.3/100000*lamda2/calculate_tan(decimal_degrees)
    # print(f"deltalamda2: {delta_lamda2}")

    delta_lamdam = 7.3/100000*lamdam/calculate_tan(decimal_degrees)
    print(f"deltalamdam: {delta_lamdam}")