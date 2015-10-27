======================================================
cmakeのメモ
======================================================
:date: 2015-10-27
:tags: cpp

make使っていたが、さすがに手間だと感じているので、cmakeにしてみる。

build周りは出来るだけモダンな状態にしておきたいからね。

とりあえず、http://www.wakayama-u.ac.jp/~chen/cmake/cmake.html をやって理解しようかと思う。

ビルド方法
----------------
プロジェクトにCMakeLists.txtを作成する。

prog1.cppというファイルをビルドするだけなら以下のような内容とする。

.. code-block:: sh

    cmake_minimum_required (VERSION 2.6)
    project (prog1)
    add_executable (prog1 prog1.cpp)

その後以下のコマンドで実行ファイルが作成, 実行できる.

.. code-block:: sh

    cmake . // Makefileを作成する
    make    // buildする
    ./prog1 // 実行する

