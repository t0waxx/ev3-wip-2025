# --- actions.py (改善後) ---
from constants import BASE_SPEED, turn_time_sp, turn_in_sp, turn_out_sp

def perform_action(action, robot):
    if action == "turn_left":
        # 左右のモーター速度を定数で指定
        robot.run_motors(turn_out_sp, turn_in_sp, duration=turn_time_sp)
    elif action == "turn_right":
        # 左右のモーター速度を定数で指定
        robot.run_motors(turn_in_sp, turn_out_sp, duration=turn_time_sp)
    elif action == "straight":
        # 直進時間も定数化するとさらに良い
        robot.run_motors(BASE_SPEED, BASE_SPEED, duration=700)
    elif action == "stop":
        print("Final checkpoint reached. Stopping.")
        return False
    return True