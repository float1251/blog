==================================================
Cordovaでandroidにアプリをinstallする
==================================================
:date: 2014-05-24
:tags: chrome, android, cordova

環境設定
-------------
手順はhttps://github.com/MobileChromeApps/mobile-chrome-apps/blob/master/README.mdにある。

    * androidSDKをインストールする。
    * .bash_profileにsdk/toolsとsdk/platform-toolsにpathを通す
    * brew install antでantを入れる。入らなかったらbrew updateしてから再度行う
    * npm install -g cca 
    * cca checkenvで怒られないことを確認

Projectの作成
----------------
以下のコマンドを実行する

    cca create APP_NAME

.. 
    Error: Cannot find module 'cordova/platforms'
    と怒られたが、--androidとつけてcreateして解決。
    iosの設定はやってないからなんか足りんかったんだろう。

実行
--------------
作成したプロジェクトディレクトリで以下を実行

    cca run android

これでアプリがdeviceにインストールされる。

プロジェクトの構造
-------------------
以下のような形になっている。

::

    .
    ├── config.xml
    ├── hooks
    │   ├── README.md
    │   ├── after_prepare
    │   └── before_prepare
    ├── merges
    │   └── android
    ├── platforms
    │   └── android
    ├── plugins
    │   ├── android.json
    │   ├── org.apache.cordova.file
    │   ├── org.apache.cordova.inappbrowser
    │   ├── org.apache.cordova.keyboard
    │   ├── org.apache.cordova.network-information
    │   ├── org.apache.cordova.statusbar
    │   ├── org.chromium.bootstrap
    │   ├── org.chromium.common
    │   ├── org.chromium.i18n
    │   ├── org.chromium.navigation
    │   ├── org.chromium.polyfill.CustomEvent
    │   ├── org.chromium.polyfill.blob_constructor
    │   ├── org.chromium.polyfill.xhr_features
    │   ├── org.chromium.runtime
    │   └── org.chromium.storage
    └── www
        ├── assets
        ├── background.js
        ├── index.css
        ├── index.html
        ├── manifest.json
        └── manifest.mobile.json

www以下がwebviewで使用されるファイル。
