# PIDゲイン
Kp = 0.53
Ki = 0.01
Kd = 0.1

# モーター設定
turn_in_sp = -20
turn_out_sp = 230
turn_time_sp = 1000

# ライン位置反転フラグ（True: 黒の右側, False: 黒の左側）
line_on_left = True

BASE_SPEED = 100

# 色判定のしきい値（RGBの範囲条件をラムダ関数で表現）
COLOR_THRESHOLDS = {
    "red": lambda r, g, b: r > 200 and g < 70  and b < 70,
    "green": lambda r, g, b: r < 70  and g > 110 and b < 90,
    "blue": lambda r, g, b: r < 60  and g < 150 and b > 130,
}

expected_path = [
    ("red", 0, "turn_left"), #1
    ("blue", 0, "turn_right"), #5
    # ("green", 0, "straight"), #skip
    ("green", 0, "turn_left"), #2
    ("red", 0, "straight"), #3
    ("green", 0, "straight"), #4
    ("red", 0, "straight"), #1
    ("green", 0, "straight"), #2
    ("red", 0, "turn_left"), #3
    ("blue", 0, "turn_right"), #5
    # ("green", 0, "straight"), #skip
    ("green", 0, "turn_right", 3), #4
    ("red", 0, "straight"), #3
    ("green", 0, "straight"), #2
    ("red", 0, "stop"), #3
]