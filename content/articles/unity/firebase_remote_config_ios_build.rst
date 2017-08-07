=============================================================
Unity Cloud BuildでFirebaseSDKを組み込んだアプリをビルドする
=============================================================
:date: 2017-08-07
:tags: Unity, Android, iOS

FirebaseのiOS版はcocoapodsを使用して各Framework等をインストールしている.

ただ残念なことにUnity Cloud Buildはcocoapodsに対応していない(マジかよ...

なので、自分で依存FrameworkをPlugins/iOS以下に入れる必要がある.

以下のブログを参考にしたが、FirebaseのドキュメントにリンクされているSDKが3.16で、最新版が4.0.4だったので自分で対応することにした.

以下の記事を参考にしながら対応していきました！

http://blog.livedoor.jp/abars/archives/52394874.html

環境
------
自分の環境は以下

* Unity5.6.1p3
* Xcode8.3.3

対応手順
----------
1. 自分のローカルPCにcocoapodsを入れる

2. Unity Firebaseを入れたUnity Projectでiosをビルドする

3. 出力したProjectのPods以下をplugins/iosにコピーする.(自分はPlugins/iOS/FireaseDependenciesにコピーした)
   
   コピーするのは以下の画像の選択されているもの.

.. image:: {filename}../../images/20170807.png
    :alt: screenshot 

4. 配置したProtobuf以下のファイルのcompile flagsに以下を設定する

..
    
    -fno-objc-arc -fobjc-exceptions

※ objc-exceptionsに関してはこれで正しいかはよくわかってないです。

5. google/protobuf以下にあるimportのpathが解決できないみたいのなので以下のようにして置き換えます.

   pathは適宜書き換えて対応してください。

.. code-block:: bash
    
    ag -l google/protobuf/ Assets/Plugins/iOS/FirebaseDependencies/Protobuf/objectivec/google/protobuf | xargs perl -pi -e 's/google\/protobuf\///g'

6. 各Editor ScriptにあるAddPodあたりの処理をコメントアウトします。
   
   以下コマンドあたりで対象ファイルを探してやるのがいいかと思います。

.. code-block:: bash
   
    ag AddPod Assets/

以上.
