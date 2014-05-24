.. ====================================================
   Rendering Benchmarks (aka Smoothness benchmarks)
   ====================================================

=========================================================
レンダリングベンチマーク(スムーズさのベンチマーク)
=========================================================

.. Contact: nduca, ernstm

.. Contace: nduca, ernstm

.. Chrome now has an awesome rendering benchmark system for GPU and rendering related benchmarks. It works on all chrome flavors, even android and CrOS, even in their content_shell forms.

Chromeは素晴らしいGPUや、ベンチマーク関連の描画のためのレンダリングベンチマークシステムを持っている。それはすべてのchromeの亜種、androidやchrome os、それらのcontent_shell forms内でも動く。


.. We use the following terminology:

以下の様な専門用語を使用する。

..  action: an interaction with a web page that we want to measure. e.g. scrolling, or simply waiting for a few seconds
    page set: a collection of web pages and associated actions
    metric: computes high-level statistical measures (e.g. means and medians) from raw data (e.g. traces).
    measurement: loads the pages from a page set, executes the associated actions, collects raw data, and computes final results using a metric.
    benchmark: bundles together a measurement and a page_set


    * action
        私達が計測したいウェブページでの作用。例えば、スクロール、何秒間の単純な待ち

    * page set
        ウェブページや関連したactionの集合

    * metric
        高レベルでの統計的な生データでの計測を解析すること

    * benchmark
        計測とpage setをまとめたもの


.. To run the rendering benchmarks you need:

レンダリングベンチマークを実行するのに必要のもの

..  * A chrome build. Just canary or a stable will work. Or download a continuous build from http://commondatastorage.googleapis.com/chromium-browser-continuous/index.html
    * python.

    * 試用版か安定版のchromeビルド。あるいはhttp://commondatastorage.googleapis.com/chromium-browser-continuous/index.htmlにある継続的ビルドをダウンロードする

    * python

.. Once you've got these things, you're ready to go. To run our top 25 page set through our smoothness measurement (which tests scrolling speed for sites that scroll, or interaction speed for sites that have interactions):
