# モック環境のセットアップと使用方法

このプロジェクトでは、PC上でEV3ロボットの動作をシミュレートするために `mock_ev3dev.py` を使用します。これにより、実機がなくても開発やテストを行うことができます。

## モック環境の概要

`mock_ev3dev.py` は以下のクラスをモックとして提供します。

- `Button`: ボタン操作のシミュレーション
- `ColorSensor`: 色センサーのシミュレーション
- `LargeMotor`: モーターのシミュレーション

## 使用方法

### 自動切り替え

`src/robot.py` では、`ev3dev.ev3` がインポートできない場合に自動的に `mock_ev3dev.py` を使用するように設定されています。そのため、特別な設定を行わずにPC上でスクリプトを実行できます。

### 手動切り替え

必要に応じて、以下のように手動でモックをインポートすることも可能です。

```python
from src.mock_ev3dev import Button, ColorSensor, LargeMotor
```

## 注意点

- モック環境はあくまでシミュレーション用であり、実機の動作と完全に一致するわけではありません。
- 実機での動作確認を行う際は、`ev3dev.ev3` を使用してください。

## テスト例

以下は、モック環境でモーターを動作させる簡単な例です。

```python
from src.mock_ev3dev import LargeMotor

motor = LargeMotor('outA')
motor.run_forever(speed_sp=500)
print("Motor is running")
motor.stop()
print("Motor stopped")
```
