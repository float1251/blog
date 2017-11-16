======================================================
appiumの環境構築
======================================================
:date: 2017-11-16
:tags: android, ios, appium

Unitynのアプリの自動操作はC#のスクリプトを書いていたが、appiumを試してみる.

個人での開発においては自動テストによる信頼性の担保がなければ規模の大きいゲームは作れないと確信したので...

クライアントはpythonを想定.

    1. python-clientをインストールする
        
        .. code-block:: bash
    
            pip install Appium-Python-Client
            // だめだった場合は以下
            sudo -H pip3 install Appium-Python-Client
    
    2. node.jsのインストール. nodeはこれでしか現状使わないので公式から落とす
    
    3. appiumのインストール

        .. code-block:: bash
            
            npm install -g appium

Androidで使う場合は以下も忘れずに.

    1. Android-SDKのインストール
    
    2. ANDROID_HOMEを設定する.
