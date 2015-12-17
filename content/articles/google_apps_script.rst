==================================================
Google apps script触ったのでまとめた
==================================================
:date: 2015-12-17
:tags: google app script

今作成しているゲームでは、データの入力をGoogle SpreadSheetで行っています。

SpreadSheetに入力された情報から、sqliteにInsertするSQLを出力するスクリプトを書きました。

その過程で調べたことをまとめようと思います。

Google apps scriptとは
^^^^^^^^^^^^^^^^^^^^^^^^^
jsライクなscript言語。というかjs。実行はサーバー側(ブラウザではない。)で行われている模様。

ツール > スクリプトエディタ と選択すると、エディタ画面が立ち上がるので、ブラウザ上で開発が出来る。

基本的な情報は以下のurlを見たほうがよいです。

http://qiita.com/soundTricker/items/4d04c97c499b22886dfd

公式のリファレンス等は以下

https://developers.google.com/apps-script/

ライブラリの導入方法
^^^^^^^^^^^^^^^^^^^^^^^
スクリプトエディター上から

リソース > ライブラリを選択。

ライブラリのkeyを貼り付けすれば、導入できる。

underscoreGSは入れておくと便利。

その他
^^^^^^^^^^^^^
- SpreadSheetを操作したい。
    - SpreadSheetAppクラスからいじる

- Cellの値を取得したいんだが。

    .. code-block:: js
    
        sheet.getRange(row, column).getValue() // Rangeの左上端の値を取得する

- ファイルを保存したいんだが.
    DriveAppクラスから作成する。

- 今操作しているSpreadSheetファイルと同じディレクトリにファイルを作成したいんだが。

    .. code-block:: js

        var id = SpreadsheetApp.getActiveSpreadsheet().getId(); // スプレッドシートのIDを取得
        var f = DriveApp.getFileById(id).getParents().next();  // 親ディレクトリを取得
        DriveApp.getFolderById(f.getId()).createFile(file_name, text); // ファイルを作成

- A11みたいなセル名で値取得できないの

    .. code-block:: js
        
        sheet.getRange("A11").getValue()

- printデバッグってどうやる？？
    使っていないCellにsetValueして表示する。

- menuを追加したいんだけど。

    .. code-block:: js
        
        var ss = SpreadsheetApp.getActiveSpreadsheet();
        var menus = [{name: "メニュー1", functionName: "functionName"}];
        ss.addMenu('メニュー名', menus);

- Alert的なのってないの？？
    Browser.msgBosとかSpreadsheetApp.getUi().alertとか使うとよい。
