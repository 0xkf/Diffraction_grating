＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝


 # https://github.com/0xkf/Diffraction_grating

```
環境構築
①Install python3

brew install python
python --version
<!-- 必要であれば、pathを通す -->

②pip3 install math

変数の設定

③inputするパラメータを直接入力。
edit input array in  physics_report.py

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
]

④強め合う波長の次数を手動で変更
edit the number m in  physics_report.py
    m = 8  # 

プログラムの実行
⑤python3 physics_report.py

```