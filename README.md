# robosys2024 課題２
[![test](https://github.com/un446/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/un446/mypkg/actions/workflows/test.yml)

## このパッケージについて
* このパッケージは2024年ロボットシステム学の課題２で作成したパッケージです。
* このパッケージに含まれるノードを用いることにより、システムステータスを出力するノードを簡単に作成できます。

## 使用方法

このリポジトリを下記のようにクローンしてください。

```
https://github.com/un446/mypkg.git
```

## memoryノード

* このノードは、以下のようにシステムのステータス情報をパブリッシュします。

```
$ ros2 run mypkg memory
[INFO] [1736000540.857201501] [system_status_publisher]: System Status Publisher Node has started.
[INFO] [1736000541.848429813] [system_status_publisher]: Publishing: "CPU: 0.6%, Memory: 4.0%, Disk: 0.6%"
[INFO] [1736000542.848363660] [system_status_publisher]: Publishing: "CPU: 0.0%, Memory: 4.0%, Disk: 0.6%"
[INFO] [1736000543.849839211] [system_status_publisher]: Publishing: "CPU: 0.0%, Memory: 4.0%, Disk: 0.6%"
```

## 開発環境
* Ubuntu 22.04 LTS
* Python 3
* ROS 2 Humble Hawksbil

## テスト環境
* Ubuntu 22.04 LTS
* ROS 2 Humble Hawksbil

## 著作権･ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* © 2024 Yuna Isomura
