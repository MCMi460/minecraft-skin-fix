from . import Proxy, Server, Thread

class SkinFixer:
    def start(*, proxy_port:int = 46653):
        proxy = Proxy(port = proxy_port)
        Thread(target = proxy.start, daemon = True).start()
        server = Server()
        server.start()
