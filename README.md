# TF-IDF計算、コサイン類似法を使ったサンプルアプリケーション

## 前提環境
python3 node.js

## 開発用ビルド
```cmd
cd {PROJECT_ROOT}/front
npm install
npm run build
```
```cmd
cd {PROJECT_ROOT}/back
python -m venv venv
.\venv\Scripts\activate
(venv) pip install -r requirements/dev.txt
(venv) python manage.py runserver
```

## プロダクションビルド
dockerつこてください  
※ dockerfile, docker-composeは[nginx-proxy](https://github.com/jwilder/nginx-proxy)と[docker-letsencrypt-nginx-proxy-companion](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion)のコンテナが立ち上がっている前提の内容になっています。
