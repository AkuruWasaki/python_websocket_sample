
### websocketsのmoduleをインストールしているのにModuleNotFoundErrorが発生.

```bash
$ python3 server.py
Traceback (most recent call last):
  File "server.py", line 2, in <module>
    import websockets
ModuleNotFoundError: No module named 'websockets'
akuruwasaki@MacBook-Pro:~/Develop/baleen_studio/python_websocket_sample
$ 
akuruwasaki@MacBook-Pro:~/Develop/baleen_studio/python_websocket_sample
$ pip3 install websockets
Collecting websockets
  Using cached websockets-10.4-cp38-cp38-macosx_10_9_x86_64.whl (97 kB)
Installing collected packages: websockets
Successfully installed websockets-10.4
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/Users/akuruwasaki/.pyenv/versions/3.8.15/bin/python3.8 -m pip install --upgrade pip' command.
```

`/Users/akuruwasaki/.pyenv/versions/3.8.15/bin/python3.8 -m pip install --upgrade pip` を実行したら解決.