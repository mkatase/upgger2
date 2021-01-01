# Upgger2 - Upgger - Google BloggerのためのHTMLアップローダ Version 2
Google BloggerのためのHTMLアップローダ。Pythonにて実装。
Google Blogger API v3対応。

## JSONファイルの設定
[このページ](https://console.developers.google.com/apis/credentials) アクセスをして、credentials.jsonファイルを入手してください。
```
$ mkdir .conf
$ cp credentials.json .conf
```

## ブログリストから対象ブログのIDを選択
```
$ ./script/list.py 
This user's display name is: carlos

 Blog Id            | Blog Title
--------------------+------------------------------------------------
1111222233334444555 | Test A Blog
6666777788889999000 | Test B Blog
$
```
"Test A Blog"を選択するなら、upgger.yamlファイルに、Blog IDを設定してください。

```
$ cat .conf/upgger.yaml
blog_id: '1111222233334444555'
```
.confディレクトリは以下のようになっています。
```
$ ls -a .conf
. .. credentials.json upgger.yaml
```

## Pythonモジュールのインストール
```
$ pip install google-api-python-client google-auth-oauthlib PyYAML
```
もしくは、
```
$ pip install -r requirements.txt
```

## 使用方法
実行初回時、ブラウザ上で、「認証」や「許可」を行ってください。成功すれば「token.pickle」ファイルが「.conf」ディレクトリに作成されます
```
$ ls -a .conf
. .. credentials.json token.pickle upgger.yaml
```

* 標準 (-iオプションは必須)
```
$ python upgger2.py -i hello.html
```
上記の場合、タイトルはファイル名(hello.html)、ラベルは無し、スケジュールは無し、ステータスはLIVE（公開）

* -tもしくは--titleオプションを追加
```
$ python upgger2.py -i hello.html -t hello
```
上記の場合、タイトルは「hello」、ラベルは無し、スケジュールは無し、ステータスはLIVE（公開）
```
$ python upgger2.py -i hello.html -t "Hello World"
$ python upgger2.py -i hello.html -t Hello\ World
```
タイトルに半角スペースがある場合、ダブルコーテーションかバックスラッシュを使用する。この場合、タイトルは「Hello World」、ラベルは無し、スケジュールは無し、ステータスはLIVE（公開）

* -lもしくは-labelオプションを追加
```
$ python upgger2.py -i hello.html -l abc,def
```
上記の場合、タイトルはファイル名、ラベルは「abc」と「def」、スケジュールは無し、ステータスは公開（LIVE）  
ラベルが複数の場合、カンマを用いて、文字を連結

* -pもしくは-pubオプションを追加
```
$ python upgger2.py -i hello.html -p 20XX-YY-ZZ
```
上記の場合、タイトルはファイル名、ラベルは無し、スケジュールは「20XX-YY-ZZ」、ステータスは公開（効果なし）

* -dもしくは--draftオプションを追加
```
$ python upgger2.py -i hello.html -d
```
上記の場合、タイトルはファイル名、ラベルは無し、ステータスはDRAFT（下書き）

## 制限
*  ~~画像ファイルはアップロードできない~~
*  ~~スケジュールは設定できない~~
* パーマリンクは設定できない

## 開発環境
* OS: Fedora 32 (5.9.15-100) on x86_64
* Python: 3.8.6
* google-api-python-client: 1.12.8
* google-auth-oauthlib: 0.4.2

## バージョン
* v0.10 2021/01/01 new creation

## ライセンス
このソフトウェアは、MITライセンスのもとで公開しています。
