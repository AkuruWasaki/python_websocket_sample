## PythonでWebSocket通信


[websockets](https://websockets.readthedocs.io/en/stable/intro/index.html)を使用してみる.

### 導入
```bash
## pip3バージョン確認
$ pip3 --version
pip 22.3.1 from /Users/akuruwasaki/Library/Python/3.8/lib/python/site-packages/pip (python 3.8)

## webSockets インストール
$ pip3 install websockets
```

### 実行
```bash
### サーバー側を起動
$ python3 server.py

### サーバー側起動の状態にてクライアント側を起動
$ python3 client.py
Hello Akuru Wasaki!
```