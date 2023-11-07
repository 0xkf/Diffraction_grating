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

# 十進数での角度からタンジェントを求める関数
def calculate_tan(decimal_degrees):
    # ラジアンに変換
    radians = math.radians(decimal_degrees)
    # タンジェントを計算
    return math.tan(radians)

# 2つの角度の合計を計算し、その平均を十進数で返す関数
def calculate_average_of_two_angles(angle1, angle2):
    # 各角度を十進数に変換
    decimal_angle1 = dms_to_decimal(*angle1)
    decimal_angle2 = dms_to_decimal(*angle2)
    # 角度を合計し、2で割る
    average_angle = (decimal_angle1 + decimal_angle2) / 2
    return average_angle

def calculate_sum_of_two_angles(angle1, angle2):
    # 各角度を十進数に変換
    decimal_angle1 = dms_to_decimal(*angle1)
    decimal_angle2 = dms_to_decimal(*angle2)
    # 角度を合計し、2で割る
    sum_angle = (decimal_angle1 + decimal_angle2) 
    return sum_angle

# 角度のペアを定義 (各ペアは度、分、秒のタプル)
angle_pairs = [
    # ((6, 46, 00), (6, 46, 30)),
    # ((13, 38, 30), (13, 39, 30)),
    # ((20, 43, 00), (20, 44, 00)),
    # ((28, 8, 30), (28, 8, 0)),
    # ((28, 10, 0), (28, 9, 30)),
    # ((36, 6, 30), (36, 7, 0)),
    # ((36, 9, 30), (36, 9, 30)),
    # ((44, 58, 30), (45, 0, 0)),
    # ((45, 5, 00), (45, 3, 00)),
    # ((55, 40, 00), (55, 35, 30)),
    # ((55, 44, 30), (55, 40, 30)),
    ((69, 59, 30), (70, 32, 00)),
    ((70, 10, 30), (70, 42, 30)),
    # ...他の角度のペアを追加
    #下記関数の mを変更することを忘れずに。
]

# 角度のペアごとに計算を行う
for angle1, angle2 in angle_pairs:
    # 2つの角度の和の十進数を計算
    sum_decimal_angle = calculate_sum_of_two_angles(angle1, angle2)
    print(f"2θ: {sum_decimal_angle}")

    # 2つの角度の平均の十進数を計算
    average_decimal_angle = calculate_average_of_two_angles(angle1, angle2)
    print(f"θ : {average_decimal_angle}")

    # 平均角度のサインを計算
    sine_value = calculate_sine(average_decimal_angle)
    print(f"sinθ: {sine_value}")

    # 平均角度のタンジェントを計算
    tan_value = calculate_tan(average_decimal_angle)
    # print(f"平均角度のtanθ: {tan_value}")

    # ==============================
    # ここを適宜変更しないと、ラムダの値を間違えるので注意。
    m = 8  # 
    # ================================
    lamdam = sine_value * 10000 / 2 / m
    print(f"lamdam: {lamdam}")
    delta_lamdam = 7.3 / 100000 * lamdam / tan_value
    print(f"Δlamdam: {delta_lamdam}")
    print(f"============================")
    # ==================================
