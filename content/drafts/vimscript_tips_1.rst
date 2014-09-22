==================
vimscript tips
==================
vimscriptをちょろっと触ったので、詰まったところをメモ。

visual modeで選択されているテキストを取得する
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
以下のようなスクリプトで取得できる。

.. code-block:: vim

    let tmp = @@
    silent normal gvy
    let selected = @@
    let @@ = tmp
 
.. このスクリプトが何をやっているのかはあとで調べる。
