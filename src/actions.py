# --- actions.py (改善後) ---
from .constants import BASE_SPEED, turn_time_sp, turn_in_sp, turn_out_sp
from .utils import log

def perform_action(action, robot):
    if action == "turn_left":
        log("Action: turn_left")
        # 左右のモーター速度を定数で指定
        robot.run_motors(turn_out_sp, turn_in_sp, duration=turn_time_sp)
    elif action == "turn_right":
        log("Action: turn_right")
        # 左右のモーター速度を定数で指定
        robot.run_motors(turn_in_sp, turn_out_sp, duration=turn_time_sp)
    elif action == "straight":
        log("Action: straight")
        robot.run_motors(BASE_SPEED, BASE_SPEED, duration=700)
    elif action == "stop":
        log("Final checkpoint reached. Stopping.")
        return False
    return True