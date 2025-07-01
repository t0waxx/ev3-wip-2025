from constants import Kp, Ki, Kd, BASE_SPEED

class LineTracer:
    def __init__(self):
        self.integral = 3
        self.previous_error = 0

    def calculate_adjustment(self, red_value):
        error = 150 - red_value
        self.integral += error
        derivative = error - self.previous_error
        self.previous_error = error
        return Kp * error + Ki * self.integral + Kd * derivative

    def get_motor_speeds(self, adjustment, line_on_left):
        if line_on_left:
            return BASE_SPEED - adjustment, BASE_SPEED + adjustment
        else:
            return BASE_SPEED + adjustment, BASE_SPEED - adjustment
