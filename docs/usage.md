# CLIツールの使い方

## main.py

`main.py` はロボット制御のエントリーポイントです。以下のサブコマンドを使用できます。

### main.py サブコマンド一覧

- `run`: 指定したルートでロボットを動作させます。
- `show`: 現在の設定を表示します。
- `list`: 利用可能なルート一覧を表示します。
- `route`: 指定したルートの詳細を表示します。

### main.py 実行例

```bash
python main.py run default
```

- `default` の部分に `params.json` に定義されたルート名を指定します。

## param_tool.py

`param_tool.py` はパラメータやルート情報を管理するためのツールです。

### param_tool.py サブコマンド一覧

- `--show-all`: 全パラメータを表示します。
- `--show-routes`: 利用可能なルート一覧を表示します。
- `--show-route-detail <route>`: 指定したルートの詳細を表示します。

### param_tool.py 実行例

```bash
python src/param_tool.py --show-all
python src/param_tool.py --show-routes
python src/param_tool.py --show-route-detail default
```
