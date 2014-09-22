=================================
Googleの画像検索APIを使ってみる
=================================
:date: 2014-06-02

現在はCustom Search APIを使用する。

https://developers.google.com/custom-search/json-api/v1/overview?hl=ja

データ型
###########
JSONかAtomで返ってくる模様。

Atomで取得する際はqueryにalt=atomとつける。

価格
########
Freeのやつと有料のやつがある。

    * Custom Search Engine
        100 requests/dayで無料。Cloud Consoleでbilingを有効化すれば、$5/1000 requestsで買える。制限は10kquery/dayらしい

    * Google Site Search
        有料版。詳細はここで。
        http://www.google.com/enterprise/search/products/gss.html#pricing_content

API KEY
###########
管理コンソールから取得してくる。

Custom Search Engine
######################
Custom Search Engine IDというものが必要らしい。

最初に設定するとき、対象のURLを入力するとあって、
全体を対象にするにはどうすればいいのかわからなかったが、

http://ryutamaki.hatenablog.com/entry/2014/01/18/171640

これ見て設定したらうまくいった。

Custom Search apiの使い方
###########################
ここ見ればわかる。

https://developers.google.com/custom-search/json-api/v1/using_rest?hl=ja

URLフォーマットは以下::

    https://www.googleapis.com/customsearch/v1?{parameters}

必須パラメータは以下3つ

    * API Key
        管理コンソールで取得したAPI Key

    * Custom Search Engine ID
        Custom Search Engineで作成したEngine Id
        今回はcxで渡せば良い模様。

    * Search Query
        検索ワードを渡せばおｋ．

その他のquery parameterはここ見ましょう。

https://developers.google.com/custom-search/json-api/v1/reference/cse/list?hl=ja#request
https://developers.google.com/custom-search/json-api/v1/using_rest?hl=ja#api-specific_query_parameters

とりあえず今回は画像検索だからsearchTypeにimageを設定する必要があるらしい。

response形式
###############
以下を参照。

https://developers.google.com/custom-search/json-api/v1/reference/cse/list?hl=ja#response

画像のリンクはitems.linkのURLを見ればいいらしい。
