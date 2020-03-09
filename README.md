# bbsrv

## 開発環境をインストール

- Ubuntu
- Ruby (rbenv)

```sh
sudo apt install libsqlite3-dev
```

```rb
# Gemfile
gem 'sqlite3', '~> 1.3', '>= 1.3.11'
```

## サーバーの起動

```sh
sudo `which ruby` server.rb
```
