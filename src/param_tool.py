import json
import os
import argparse
from pprint import pprint

PARAMS_PATH = os.path.join(os.path.dirname(__file__), 'params.json')

def show_all_params():
    with open(PARAMS_PATH, encoding='utf-8') as f:
        params = json.load(f)
    pprint(params)

def show_routes():
    with open(PARAMS_PATH, encoding='utf-8') as f:
        params = json.load(f)
    print("利用可能なルート一覧:")
    for route in params['routes']:
        print(f"- {route}")

def show_route_detail(route_name):
    with open(PARAMS_PATH, encoding='utf-8') as f:
        params = json.load(f)
    route = params['routes'].get(route_name)
    if route is None:
        print(f"ルート '{route_name}' は存在しません")
    else:
        print(f"ルート '{route_name}' の詳細:")
        for i, step in enumerate(route, 1):
            print(f"  {i}: {step}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--show-all', action='store_true', help='全パラメータを表示')
    parser.add_argument('--show-routes', action='store_true', help='ルート一覧を表示')
    parser.add_argument('--show-route-detail', type=str, help='指定ルートの詳細を表示')
    args = parser.parse_args()

    if args.show_all:
        show_all_params()
    elif args.show_routes:
        show_routes()
    elif args.show_route_detail:
        show_route_detail(args.show_route_detail)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
