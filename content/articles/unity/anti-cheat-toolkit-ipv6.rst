=============================================================
Anti-Cheat ToolkitのTimecheatingDetectorがIPV6で動作しない
=============================================================
:date: 2017-09-27
:tags: Unity, iOS

versionは1.5.6.1.

ipv6環境ではErrorダイアログが出続ける.
TimeCheatingDetector.csの以下の部分を変更する.

.. code-block:: c#

    // 元々
	// var socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
    // 変更後
	var socket = new Socket(addresses[0].AddressFamily, SocketType.Dgram, ProtocolType.Udp);

IPV6のテスト方法は以下を参照.

http://qiita.com/yonell/items/16c08e541b4a2b84b0a3
