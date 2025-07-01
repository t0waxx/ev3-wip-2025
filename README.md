# EV3 Robot Control Project

## 概要

このプロジェクトは、EV3ロボットを制御するためのPythonプログラムです。ロボットの動作、パラメータ管理、ルート設定などを柔軟に行うことができます。

## ディレクトリ構成

```plaintext
.
├── main.py                # エントリーポイント
└── src
    ├── __init__.py        # パッケージ初期化
    ├── actions.py         # アクション管理
    ├── constants.py       # 定数とパラメータ管理
    ├── detector.py        # 色検出ロジック
    ├── mock_ev3dev.py     # PC用モック
    ├── param_tool.py      # パラメータ管理ツール
    ├── params.json        # パラメータ設定ファイル
    ├── robot.py           # ロボット制御クラス
    ├── tracer.py          # ライントレーサーロジック
    └── utils.py           # ユーティリティ関数
```

## 主な機能

### 1. ロボット制御

`main.py` を使用してロボットを制御します。

#### 実行例（ロボット制御）

```bash
python main.py run default
```

- `default` の部分に `params.json` に定義されたルート名を指定します。

### 2. パラメータ管理

`param_tool.py` を使用してパラメータを管理します。

#### 実行例（パラメータ管理）

```bash
python src/param_tool.py --show-all       # 全パラメータを表示
python src/param_tool.py --show-routes   # ルート一覧を表示
python src/param_tool.py --show-route-detail default  # 指定ルートの詳細を表示
```

### 3. モック環境

`mock_ev3dev.py` を使用して、PC上でロボットの動作をシミュレートできます。

## パラメータ設定

`params.json` にロボットの動作やルート設定を記述します。

### params.json の例

```json
{
  "pid": {
    "Kp": 0.53,
    "Ki": 0.01,
    "Kd": 0.1
  },
  "motor": {
    "turn_in_sp": -20,
    "turn_out_sp": 230,
    "turn_time_sp": 1000,
    "base_speed": 100
  },
  "line_on_left": true,
  "color_thresholds": {
    "red": {"r_min": 201, "g_max": 69, "b_max": 69},
    "green": {"r_max": 69, "g_min": 111, "b_max": 89},
    "blue": {"r_max": 59, "g_max": 149, "b_min": 131}
  },
  "routes": {
    "default": [
      ["red", 0, "turn_left"],
      ["blue", 0, "turn_right"],
      ["green", 0, "turn_left"],
      ["red", 0, "straight"],
      ["green", 0, "straight"],
      ["red", 0, "straight"],
      ["green", 0, "straight"],
      ["red", 0, "turn_left"],
      ["blue", 0, "turn_right"],
      ["green", 0, "turn_right", 3],
      ["red", 0, "straight"],
      ["green", 0, "straight"],
      ["red", 0, "stop"]
    ]
  }
}
```

## 開発・テスト

- 実機での動作確認には `ev3dev.ev3` を使用します。
- PC上での開発・テストには `mock_ev3dev.py` を使用します。

## 必要な環境

- Python 3.7以上
- `ev3dev` ライブラリ（実機使用時）

## ライセンス

MIT License

## 詳細ドキュメント

プロジェクトの詳細な仕様や使用方法については、以下のドキュメントをご参照ください：

- [CLIツールの使い方](docs/usage.md)
- [params.json の詳細](docs/parameters.md)
- [モック環境のセットアップと使用方法](docs/mock_environment.md)
- [開発とテストの手順](docs/development.md)
