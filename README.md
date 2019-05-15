# サンプルアプリケーション

## アプリケーション一覧
- ポケモン検索  
    TF-IDF計算、cos類似法を使ったあいまい単語検索、種族値の類似検索機能

### [デモ](https://apps.yu-tsuchiya.me/)(そのうち消えます)

### ディレクトリ構成
```
root/
  ├─back/ バックエンドのソースコード+デプロイ用の設定ファイル。pythonのDjangoを使っています。
  ├─front/ フロントエンドのソースコード。vue, vuetifyで作っています。
  └─scraping/ 学習用データをwebサイトから取得するためのpythonスクリプトが置いてあります。
```

## ローカルで起動する場合
### 前提条件
- 以下がインストール済
    - python3
    - node.js
    - Mecab ※インストール時の文字コードにutf-8を指定してください  
### 手順
1. フロントエンドのコードをビルドする(back配下に静的ファイルを出力)
    ```cmd
    cd {PROJECT_ROOT}/front
    npm install
    npm run build
    ```
1. サーバを立ち上げる(開発者モード)
    ```cmd
    cd {PROJECT_ROOT}/back
    python -m venv venv
    .\venv\Scripts\activate
    (venv) pip install -r requirements/dev.txt
    (venv) python manage.py runserver
    ```
    ※開発者モードはwindows上でのみ動作します。(pythonの依存にwindows用のライブラリがあるため)  

## デプロイ
### 前提条件
- デプロイ環境にdocker, docker-composeインストール済み
- 独自ドメイン取得済み

### 手順
1. ローカルでfrontをビルド
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
