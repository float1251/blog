=============================================================
Very Simple Ads Monetization & Mediationに細かな修正を加える
=============================================================
:date: 2017-10-19
:tags: Unity, Android, iOS, admob, adcolony

動画広告を表示するのにVery Simple AdsというAssetを購入し、使用している.

https://www.assetstore.unity3d.com/jp/#!/content/57517

基本的にこれを入れてやればいいが、以下の2点の対応のために修正を加えた.

    1. adcolonyの動画広告視聴前後に、ダイアログが表示される
    
    2. admobの動画広告視聴完了時に、エラーが頻発する

ので、以下の対応を行った。

1. AAAdcolonyの200行目くらいの箇所を以下のように修正する

.. code-block:: C#

    AdColony.AdOptions adOptions = new AdColony.AdOptions ();
    // 以下2つをfalseに変更
    adOptions.ShowPrePopup = false;
    adOptions.ShowPostPopup = false;

2. Admobのエラー回避

https://github.com/googleads/googleads-mobile-unity/issues/509

↑のissueと同様に、OnAdRewardが呼ばれた直後にOnAdCloseが呼ばれていた.

そのため、OnAdRewardが呼ばれたらflagを立てて、OnAdCloseが呼ばれても大丈夫なように対応した.
