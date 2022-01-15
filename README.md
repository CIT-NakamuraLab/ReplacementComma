# ReplacementComma
、。を，．に置換する

Texを書いていて「、。」を「，．」に置換するのがめんどくさいので作りました。
論文があるディレクトリを指定すると、そこから再帰的に`*.tex`ファイルを探して置換してくれます。

**このスクリプトはバックアップを取らないので、必要なら自分でバックアップとってください。**

## 使い方

まずはcloneしてください

```
$ git clone https://github.com/CIT-NakamuraLab/ReplacementComma.git
```

コマンドライン引数で置換したいtexファイルがあるパスを指定します。
置換される`*.tex`ファイルの一覧がでるので、それを置換しても良い場合は`y`を入力して置換を開始します。

```pyton
$ python3 main.py ~/GitHub/sakurai-thesis/
dir path: /Users/takumi/GitHub/sakurai-thesis/
tex file: [ここに.texファイルの一覧がリストで表示される]
置換を開始しても良いですか？ (y/n): y
success!!
```

引数を指定しないとエラーメッセージが出ます。

```python
$ python3 main.py
error
usage: python main.py [directory]
```

引数の最後に`/`をつけていない場合もエラーになります。

```
$ python3 main.py ~/GitHub/sakurai-thesis
dir path: /Users/takumi/GitHub/sakurai-thesis
error
no tex file found
```
