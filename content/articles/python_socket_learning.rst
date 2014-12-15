========================================
pythonでsocketプログラミングをやってみる
========================================
:date: 2014-12-15
:tags: python

pythonでsocketプログラミングをやってみる。

とりあえず簡単なTCPクライントとServerを作成する。

使用するのはpython3.3.5.

ここあたりはとりあえず読んでおく。

http://docs.python.jp/3.3/howto/sockets.html

client側コード

.. code-block:: python

    import socket
    
    target_host = "localhost"
    target_port = 9999
    
    # create socket object
    # AF_INET -> ipv4を使います
    # SOCK_STREAM -> tcpを使います
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((target_host, target_port))
    
    # strではなくbyteを渡す
    client.send(b"Hello Server")
    
    response = client.recv(4096)
    
    print(response.decode())
    
    client.close()

server側コード

.. code-block:: python

    import socketserver
    
    
    class MyTCPHandler(socketserver.BaseRequestHandler):
        """
        socket server request handler
        """
    
        def setup(self):
            print("request Started")
    
        def handle(self):
            # self.rquest is TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print("{} worte:".format(self.client_address[0]))
            print(self.data)
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())
    
        def finish(self):
            print("request finished")
    
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
    
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    
        server.serve_forever()

これでサーバーを起動してからクライントを実行すればよい。
