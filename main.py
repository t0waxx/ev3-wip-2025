import time
import argparse
from src.robot import Robot
from src.tracer import LineTracer
from src.detector import ColorDetector
from src.actions import perform_action
from src.constants import get_route_from_args, line_on_left
from src.utils import log
from src.param_tool import show_all_params, show_routes, show_route_detail

def run_main(route_name):
    expected_path = get_route_from_args(route_name)
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

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # runサブコマンド
    # ロボットを指定したルートで動作させる
    run_parser = subparsers.add_parser('run', help='ロボットを動かす')
    run_parser.add_argument('route', type=str, help='params.jsonのルート名')

    # showサブコマンド
    # 全パラメータを表示する
    subparsers.add_parser('show', help='全パラメータを表示')

    # listサブコマンド
    # 利用可能なルート一覧を表示する
    subparsers.add_parser('list', help='ルート一覧を表示')

    # routeサブコマンド
    # 指定したルートの詳細を表示する
    route_parser = subparsers.add_parser('route', help='指定ルートの詳細を表示')
    route_parser.add_argument('route_name', type=str, help='ルート名')

    args = parser.parse_args()

    if args.command == 'run':
        run_main(args.route)
    elif args.command == 'show':
        show_all_params()
    elif args.command == 'list':
        show_routes()
    elif args.command == 'route':
        show_route_detail(args.route_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()