vimscriptについて
===================
:date: 2014-05-11

vim pluginを開発したいと考えているが、まずはvimscriptについて知らないといけない。

ということでちょっと調べてみた。

http://mattn.kaoriya.net/software/vim/20111202085236.htm

この記事が素晴らしすぎたので、こっちを読むとよいと思います。

あとこことか

http://vim-users.jp/2010/04/hack136/
http://vim-jp.org/tips/start_vimscript.html

とりあえず、備忘録的にやったことを残しておこうと思います。

変数宣言
-----------
こんな感じ。

.. code-block:: vim

    " 数値
    let foo = 1
    " 文字列
    let foo = "bar"
    " リスト
    let foo = ["foo", "bar"]
    " 辞書
    let foo = {"bar": "bar"}

関数定義
------------
こんな感じ。

.. code-block:: vim

    function Foo()
        echo "foo"
    endfunction

コマンドラインから実行すると以下のようになる。

.. code-block:: vim

    :call Foo()
    foo

同じ関数名を定義するにはfunction!を指定する

.. code-block:: vim

    function! Foo()
        echo "foo"
    endfunction

スコープ
------------
関数内で有効なローカルスコープ l:、スクリプトファイル内で有効なスコープ s:、グローバルで有効なスコープ、
がよく使う。

こんな感じ。

.. code-block:: vim

    function! s:Foo()
        let l:foo = "foo"
        echo foo
    endfunction
    call s:Foo()

Pythonインターフェース
------------------------
vimscriptではPythonを使用することが出来ます。

まずは使用できるかどうかの確認。

.. code-block:: vim

    echo has("python")
    1
    
    echo has("python3")
    1
    
であればpython2もpython3も両方使えます。

ではvimscriptで実際にpythonを使用してみます。

.. code-block:: vim

    function! s:Foo()
        python3 << EOM
    print("foo")
    EOM
    endfunction

    call s:Foo()

このような形で使用します。

外部ファイルを実行する際は:pyfileコマンドを使用します。

map
--------
基本的なコマンドについては知っているので割愛。

インサートモードにおいて、関数の評価結果から入力文字列を挿入させるためには<expr>を使用する。

.. code-block:: vim
    
    inoremap <expr> <c-x> Foo()

command
----------
コマンドモードから実行できるコマンドを定義する。

名前の戦闘は大文字である必要がある。

.. code-block:: vim

    command! Foo :call Foo()

詳しくは help :command-args を参照。

autoloadとautocmd
-------------------
http://mattn.kaoriya.net/software/vim/20111202085236.htm

ここ見たほうがよいです。

vimscriptの組み込み関数
-------------------------
機能別に分類してあるヘルプは以下で見れる。

.. code-block:: vim

    :help function-list

アルファベット順は以下

.. code-block:: vim

    :help functions

ということで最後の方はだいぶ適当になったけど、これで最低限vimscriptが読めるようになった気がします。

あとは色々見たり作ったりしながら覚えていこうかと思います。
