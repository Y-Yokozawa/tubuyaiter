# Python講座 デプロイハンズオン向け Djangoアプリ
## つぶやきアプリ（tubuyaiter）
=========

## 環境
- Python 3.8.0
- Django 3.1.1

## 前準備
ソースコードのCloneをします。
```
$ git clone https://github.com/jsl-webcourse/tubuyaiter.git
```

仮想環境を作成し、以下を実行します。
venvの場合
```
$ cd tubuyaiter
$ python3.8 -m venv env 
$ source env/bin/activate
```

```
$ pip install -r requirements.txt
```

マイグレーションをする
```
$ python manage.py migrate
```

test
