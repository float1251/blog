tsdの使い方
==============
久しぶりにtsdを触ったらだいぶ使い方が変わっていたのでメモを残しておく。

tsdのinstall
----------------
現在開発中の0.6系はコマンドがだいぶ変わっているが、今回は0.6.x系を使用するので以下のようにしてinstallする.

..code-block::
    
    npm install tsd@next -g

tsd.jsonの作成
----------------
configファイルであるtsd.jsonを作成する。

.. code-block::

    tsd init

d.tsのinstall
--------------
definitlytypedにあるd.tsをinstallする.

.. code-block::
    
    tsd install underscore --save

definitlytypedにないd.tsを管理する
--------------------------------------
tsd linkコマンドを使用して管理することができるはずなのだが、README通りにやってもできなかった。。。

そもそもpackage.jsonの読み込みができてなさ気な感じだから、ちょっとソース読まないとわかんないな。。。

ここは後で再度試す。
