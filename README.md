# サンプルアプリケーション

### [デモ](https://apps.yu-tsuchiya.me/)(そのうち消えます)

## アプリケーション一覧
- ポケモン検索  
    TF-IDF計算、cos類似法を使ったあいまい単語検索、種族値の類似検索機能  
    ロジックは`back/pokemon/pokemon_service.py`にあります。

### ディレクトリ構成
```
root/
  ├─back/ バックエンドのソースコード+デプロイ用の設定ファイル。pythonのdjangoを使っています。
  ├─front/ フロントエンドのソースコード。vue, vuetifyを使っています。
  └─scraping/ 学習用データをwebサイトから取得するためのpythonスクリプトが置いてあります。
```

## ローカルで起動する場合
### 前提条件
- OSがWindows (開発用のpython依存関係にwindows用のライブラリがあるため)
- 以下がインストール済
    - python3
    - node.js
    - [Mecab](https://taku910.github.io/mecab/) ※インストール時の文字コードにutf-8を指定してください  
### 手順
1. development modeでdjangoサーバ立ち上げ
    ```cmd
    cd {PROJECT_ROOT}/back
    python -m venv venv
    .\venv\Scripts\activate
    (venv) pip install -r requirements/dev.txt
    (venv) python manage.py runserver
    ```
1. webpack-dev-server立ち上げ
    ```cmd
    cd {PROJECT_ROOT}/front
    npm install
    npm run serve
    ```
1. `localhost:8080`にアクセス

## デプロイ
### 前提条件
- デプロイ環境にdocker, docker-composeインストール済み
- 独自ドメイン取得済み

### 手順
1. ローカルで以下のコマンドを実行します。
    ```
    cd {PROJECT_ROOT}/front
    npm install
    npm run build
    ```
1. `back`下の`.env.sample`ファイルを`.env`に書き換えます。
1. 書き換えた`.env`ファイル内のプロパティを書き換えます。  
    `www.hoge.com`->独自ドメイン  
    `hogehoge@gmail.com`->任意のメールアドレス
1. `back`下の`proxy.sample`フォルダ名を`proxy`に書き換えます。
1. `back/proxy/conf/`下の`www.hoge.com`ファイルの名前を独自ドメインに書き換えます。
1. backフォルダをデプロイ環境にコピー
1. デプロイ環境で`docker volume create --name=appstatic`、`docker network create -d bridge proxy`実行
1. デプロイ環境で`back/proxy.sample`に移動し、`docker-compose up -d`
1. デプロイ環境で`back`に移動し、`docker-compose up -d`
1. サーバが立ち上がるので、独自ドメインにアクセスしてみてください。
