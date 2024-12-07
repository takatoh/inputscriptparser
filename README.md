# inputscriptparser

A parser for script-style input data.

プログラムの入力データをパースするパーサです。

"script-style" とは、一つずつ命令を実行しながら入力データ（の内部表現）を組み立てることを意味しています。近い例として Dockerfile が挙げられます。

## Install

pip でインストールできます：

    $ pip install inputscriptparser

または、パッケージマネージャーを使ってプロジェクトに追加します：

    $ poetry add inputscriptparser

## Usage

このパーサは、テキスト入力を命令とその引数からなるタプルのリストに変換します。

```Python
from inputscriptparser import Parser

input_data = '''CMD1 "example data"
CMD2 1 2 3
NO-ARG-CMD
'''

parser = Parser()
script = parser.parse(input_data)
```

上の例では、入力をパースした `script` は次のようになります。

```Python
[
    ('CMD1', ['example data']),
    ('CMD2', [1.0, 2.0, 3.0]),
    ('NO-ARG-CMD', [])
]
```

各命令を実行する評価器は利用者が用意する必要があります。

## Syntax

文法は次の通りです。

1. 入力データ全体を表す `script` は1個以上の文 `statement` から成ります。
2. 文 `statement` は命令 `command` と0個以上の引数 `arg` から成ります。
3. 命令と各引数は空白文字で区切られます。
4. 命令は必ず行の先頭から始まります。行が空白文字で始まる場合、その行は前の行の継続行とみなされます。
5. `//` から行末まではコメントとして無視されます。また、空行と空白文字のみの行も無視されます。

### Command

命令 `command` はラテン文字の大文字、数字、`-` から成り、必ず大文字で始まります。

### Values

引数の値として、次の型が使用できます。

- 数値
- 文字列
- 真偽値
- キーワード

数値は整数と実数を区別しません。すべて実数になります。

文字列は `" "` （ダブルクォーテーション）で囲みます。

真偽値は、真および偽とみなせる小文字の単語が使用できます。

- `true` / `false`
- `yes` / `no`
- `on` / `off`

キーワードは、ラテン文字の大文字、数字から成り、必ず大文字で始まります。命令と似ていますが、行の先頭には現れないことで区別されます。
