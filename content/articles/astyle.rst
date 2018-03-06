======================================================
C#のコードフォーマットをastyleでやったときのメモ
======================================================
:date: 2018-03-06
:tags: Unity, C#

astyleを使用してcodeformatを行う.  
http://astyle.sourceforge.net/

インストールはHomebrew経由でできた

.. code-block:: sh

    brew install astyle

以下のようにすれば指定したディレクトリ以下のcsファイルに対してフォーマットがかけられる.

.. code-block:: sh

    # findとgrepでフォーマットかけたいファイルを抽出.
    # xargsで引数としてastyleを実行.
    find Assets -type f | grep  \.cs$ | xargs -I@ astyle --options=.astyleoption @

オプションファイルの中身は以下の通り.:: 

    # c#のファイルとして認識する
    mode=cs
    # allmanスタイルにする
    style=allman
    # インデントにタブを使う
    indent=tab=4
    # 継続行のインデントにもタブを使う(但し偶数個のタブでないときはwhite spaceで埋められる)
    indent=force-tab=4
    # namespace文の中をインデントする
    indent-namespaces
    # switch文の中をインデントする
    indent-switches
    # case文の中をインデントする
    indent-cases
    # 1行ブロックを許可する
    keep-one-line-blocks
    # 1行文を許可する
    keep-one-line-statements
    # プリプロセッサをソースコード内のインデントと合わせる
    indent-preproc-cond
    # if, while, switchの後にpaddingを入れる
    pad-header
    # 演算子の前後にpaddingを入れる
    pad-oper
    # originalファイルを生成しない
    suffix=none
    # if, for, while文の前後に空行を入れる
    break-blocks
    # コメントもインデントする
    indent-col1-comments
