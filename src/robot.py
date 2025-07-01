try:
    import ev3dev.ev3 as ev3
except ImportError:
    from . import mock_ev3dev as ev3

class Robot:
    def __init__(self):
        self.button = ev3.Button()
        self.color = ev3.ColorSensor()
        self.motor_b = ev3.LargeMotor('outB')
        self.motor_c = ev3.LargeMotor('outC')

    def run_motors(self, speed_b, speed_c, duration=None):
        if duration:
            self.motor_b.run_timed(speed_sp=speed_b, time_sp=duration, stop_action='brake')
            self.motor_c.run_timed(speed_sp=speed_c, time_sp=duration, stop_action='brake')
            self.motor_b.wait_while('running')
            self.motor_c.wait_while('running')
        else:
            self.motor_b.run_forever(speed_sp=speed_b)
            self.motor_c.run_forever(speed_sp=speed_c)

    def stop_motors(self):
        self.motor_b.stop(stop_action='brake')
        self.motor_c.stop(stop_action='brake')

    def button_pressed(self):
        return self.button.backspace

    def get_rgb(self):
        return self.color.red, self.color.green, self.color.blue

    def get_red(self):
        return self.color.red