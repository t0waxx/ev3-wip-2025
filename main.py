from src.robot import Robot
from src.tracer import LineTracer
from src.detector import ColorDetector
from src.actions import perform_action
from src.constants import expected_path, line_on_left
from src.utils import log
import time

def main():
    robot = Robot()
    tracer = LineTracer()
    detector = ColorDetector()
    path_index = 0
    last_color = None

    try:
        while True:
            if robot.button_pressed():
                log("Backspace pressed. Exiting...")
                break

            red = robot.get_red()
            adjustment = tracer.calculate_adjustment(red)
            speed_b, speed_c = tracer.get_motor_speeds(adjustment, line_on_left)

            r, g, b = robot.get_rgb()
            current_color = detector.detect(r, g, b)
            log(f"Detected: {current_color}")

            if current_color != "linetrace mode" and current_color != last_color:
                last_color = current_color

                if path_index < len(expected_path):
                    target_color, delay, action = expected_path[path_index]
                    if current_color == target_color:
                        robot.stop_motors()
                        time.sleep(delay)

                        if not perform_action(action, robot):
                            break
                        path_index += 1
            else:
                robot.run_motors(speed_b, speed_c)

            time.sleep(0.1)

    except KeyboardInterrupt:
        log("KeyboardInterrupt detected. Exiting...")
    finally:
        robot.stop_motors()

if __name__ == "__main__":
    main()