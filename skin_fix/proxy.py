from . import *

class Proxy:
    def __init__(self, *, port:int = 46653):
        self.host = '127.0.0.1'
        self.port = port
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))
    
    def fetch_url(path, cape): # Code Python-ized from original @emilyploszaj project
        a = search('/Minecraft%s/([a-zA-Z0-9_]+).png' % ('Cloaks' if cape else 'Skins'), path)
        if not a:
            a = search(r'\/cloak\/get\.jsp\?user=([a-zA-Z0-9_]+)'
                if cape else
                'net/skin/([a-zA-Z0-9_]+).png', path
            )
        if not a: raise Exception()
        s = a[1]

        # Skin/cape injector
        i = Minecraft.Cloak.names if cape else Minecraft.Skin.names
        src = None
        if s in i:
            match i[s][0]:
                case 0:
                    s = i[s][1]
                case 1:
                    src = '/texture/' + i[s][1]

        j = get('https://api.mojang.com/users/profiles/minecraft/' + s).json()
        uuid = j['id']
        j = get('https://sessionserver.mojang.com/session/minecraft/profile/' + uuid).json()
        value = j['properties'][0]['value']#I hope there's only ever one
        j = loads(b64decode(value).decode('UTF-8'))
        url = j['textures']['CAPE' if cape else 'SKIN']['url']
        return url[7:29], src if src else url[29:]

    def handle_response(self, client, server):
        while True:
            data = server.recv(1024)
            if len(data) > 0:
                client.sendall(data)
            else:
                break
        server.close()

    def handle_request(self, client):
        request = b''
        client.setblocking(False)
        while True:
            try:
                data = client.recv(1024)
                request += data
            except:
                break
        try:
            message = request.decode('UTF-8')
        except:
            pass
        
        if 'MinecraftSkins' in message or 'minecraft.net/skin/' in message:
            url = Proxy.fetch_url(message, False)
        elif 'MinecraftCloaks' in message or 'minecraft.net/cloak/' in message:
            url = Proxy.fetch_url(message, True)
        else:
            url = None
            host = '52.216.109.61'
        
        if url is not None:
            host = url[0]
            request = 'GET {0} HTTP/1.1\r\nHost: {1}\r\nConnection: close\r\n\r\n'.format(
                url[1],
                host
            ).encode('UTF-8')

        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host, 80))
        server.sendall(request)
        self.handle_response(client, server)

        client.close()

    def start(self):
        print('Proxy starting on {0}:{1}...'.format(self.host, self.port))
        self.server.listen()
        while True:
            client, addr = self.server.accept()
            Thread(
                target = self.handle_request,
                args = (client,),
                daemon = True
            ).start()
