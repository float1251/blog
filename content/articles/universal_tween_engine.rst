======================================================
libgdxでuniversal tween engine使ってみた
======================================================
:date: 2015-03-03
:tags: java, libgdx

Tweenアニメーションの実装に、universal tween engineというライブラリを使ったみた。

導入はlibgdxのwikiにあった。urlは以下の通り。
    
    https://github.com/libgdx/libgdx/wiki/Universal-Tween-Engine

1. jarをtween engineの公式から落とす

2. projectのrootにlibsディレクトリを作成して、そこにjarを入れる

3. gradleの設定を変更する

実装は以下のような感じでやった。

1. Accessorを定義する。

2. アニメーションを定義する

3. renderでmanagerをupdateする

サンプルはなくしちゃった。。。(´；ω；｀)
