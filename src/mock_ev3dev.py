# mock_ev3dev.py
# PC開発・テスト用のev3dev.ev3モック
import random

class Button:
    @property
    def backspace(self):
        return False  # テスト用は常にFalse

class ColorSensor:
    @property
    def red(self):
        return random.randint(0, 255)
    @property
    def green(self):
        return random.randint(0, 255)
    @property
    def blue(self):
        return random.randint(0, 255)

class LargeMotor:
    def __init__(self, port):
        self.port = port
    def run_timed(self, speed_sp, time_sp, stop_action):
        print(f"[MOCK] run_timed({self.port}, speed_sp={speed_sp}, time_sp={time_sp}, stop_action={stop_action})")
    def run_forever(self, speed_sp):
        print(f"[MOCK] run_forever({self.port}, speed_sp={speed_sp})")
    def stop(self, stop_action):
        print(f"[MOCK] stop({self.port}, stop_action={stop_action})")
    def wait_while(self, state):
        print(f"[MOCK] wait_while({self.port}, state={state})")
