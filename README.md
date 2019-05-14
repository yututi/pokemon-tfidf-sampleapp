# TF-IDF計算、コサイン類似法を使ったサンプルアプリケーション

[デモ](https://apps.yu-tsuchiya.me/)(そのうち消えます)

## ローカルで起動する場合
### 前提環境
- python3
- node.js
- Mecab ※インストール時の文字コードにutf-8を指定してください
windows上でのみ動作します。(pythonの依存にwindows用のライブラリがあるため)  

### 手順
1. フロントエンドのコードをビルドする
    ```cmd
    cd {PROJECT_ROOT}/front
    npm install
    npm run build
    ```
1. デバッグサーバを立ち上げる
    ```cmd
    cd {PROJECT_ROOT}/back
    python -m venv venv
    .\venv\Scripts\activate
    (venv) pip install -r requirements/dev.txt
    (venv) python manage.py runserver
    ```

## デプロイ
### 前提条件
- デプロイ環境にdocker, docker-composeインストール済み
- 独自ドメイン取得済み

### 手順
1. ローカルでfrontをビルド
1. `back/proxy.sample/conf/`下の`www.hoge.com`ファイルの名前を独自ドメインに書き換えます。
1. backフォルダをデプロイ環境にコピー(zipしてね)
1. デプロイ環境で`docker volume create --name=appstatic`、`docker network create -d bridge proxy`実行
1. デプロイ環境で`back/proxy.sample`に移動し、`docker-compose up -d`
1. デプロイ環境で`back`に移動し、`docker-compose up -d`
1. サーバが立ち上がるので、独自ドメインにアクセスしてみてください。
