===========================================
vimscriptを書いてて、詰まったところ
===========================================

pyfileで引数を渡す方法
------------------------------
pythonであれば

.. code-block::
    
    python sample.py test

という形で実行するがvimではpyfileでpythonファイルを実行できるが、以下の様なやり方ではダメ。

.. code-block::

    pyfile sample.py test

こうではなく、以下の様にして引数を渡す

.. code-block::

    :python import sys
    " pythonではsys.argvの0番目はスクリプトのファイル名
    :python sys.argv = ["sample.py", "test"]
    :pyfile sample.py

こうすると想定どおりに引数がpython側で受け取れる。

python側でvimで定義した変数を受け取る
--------------------------------------
vimscriptの変数をpython側で受け取るにはvim.evalを使用する。

.. code-block:: vim

    let tmp = "Test"
    python << EOM
    import vim
    print(vim.eval("tmp"))
    EOM

こんな感じ

vimでの文字列連結
-------------------
文字列連結でつい"sample"+"test"とか書きがちだが、.(ドット)でつなげる。

.. code-block:: vim

    let a = "sample"
    let b = "test"
    echo a.b

ユーザ定義commandの引数を関数に渡す
-----------------------------------
<f-args>を使う。

詳細は:h <f-args>で。

Gvimかどうかの判定
-------------------
has("gui_running")でできる

.. code-block:: vim
    
    echo has("gui_running")
    1


こんな感じかな。
vimpluginを書くときはまず、:h vim-scriptと:h write-pluginあたりを読むほうがその後が楽だなと思った。
