# params.json の詳細

`params.json` はロボットの動作やルート設定を管理するための設定ファイルです。以下に各セクションの詳細を説明します。

## pid

PID制御のパラメータを設定します。

- `Kp`: 比例ゲイン
- `Ki`: 積分ゲイン
- `Kd`: 微分ゲイン

## motor

モーターの動作設定を管理します。

- `turn_in_sp`: 内側モーターの速度
- `turn_out_sp`: 外側モーターの速度
- `turn_time_sp`: ターン時の時間（ミリ秒）
- `base_speed`: 基本速度

## line_on_left

ラインが左側にあるかどうかを指定します。

- `true`: 左側
- `false`: 右側

## color_thresholds

色検出の閾値を設定します。

- `red`: 赤色の閾値（`r_min`, `g_max`, `b_max`）
- `green`: 緑色の閾値（`r_max`, `g_min`, `b_max`）
- `blue`: 青色の閾値（`r_max`, `g_max`, `b_min`）

## routes

ルート情報を定義します。各ルートは以下の形式で記述されます。

```json
["<色>", <距離>, "<動作>", <オプション>]
```

- `<色>`: 色検出の条件（例: `red`, `green`, `blue`）
- `<距離>`: 距離条件（未使用の場合は `0`）
- `<動作>`: 実行する動作（例: `turn_left`, `turn_right`, `straight`, `stop`）
- `<オプション>`: オプションのパラメータ（例: 繰り返し回数）

### 例

```json
"default": [
  ["red", 0, "turn_left"],
  ["blue", 0, "turn_right"],
  ["green", 0, "straight"],
  ["red", 0, "stop"]
]
```
