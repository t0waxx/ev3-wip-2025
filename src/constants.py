import json
import os
import sys
import argparse

PARAMS_PATH = os.path.join(os.path.dirname(__file__), 'params.json')

with open(PARAMS_PATH, encoding='utf-8') as f:
    _params = json.load(f)

Kp = _params['pid']['Kp']
Ki = _params['pid']['Ki']
Kd = _params['pid']['Kd']

turn_in_sp = _params['motor']['turn_in_sp']
turn_out_sp = _params['motor']['turn_out_sp']
turn_time_sp = _params['motor']['turn_time_sp']
BASE_SPEED = _params['motor']['base_speed']

line_on_left = _params['line_on_left']

COLOR_THRESHOLDS = {
    'red': lambda r, g, b: r >= _params['color_thresholds']['red']['r_min'] and g <= _params['color_thresholds']['red']['g_max'] and b <= _params['color_thresholds']['red']['b_max'],
    'green': lambda r, g, b: r <= _params['color_thresholds']['green']['r_max'] and g >= _params['color_thresholds']['green']['g_min'] and b <= _params['color_thresholds']['green']['b_max'],
    'blue': lambda r, g, b: r <= _params['color_thresholds']['blue']['r_max'] and g <= _params['color_thresholds']['blue']['g_max'] and b >= _params['color_thresholds']['blue']['b_min'],
}

def get_route_from_args(route_name='default'):
    return _params['routes'][route_name]