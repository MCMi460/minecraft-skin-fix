from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from re import search
from requests import get
from json import loads
from base64 import b64decode

def fetch_url(path, cape): # Code Python-ized from original @emilyploszaj project
    a = search('/Minecraft%s/([a-zA-Z0-9_]+).png' % ('Cloaks' if cape else 'Skins'), path)
    if not a: raise Exception()
    s = a[1]
    j = get('https://api.mojang.com/users/profiles/minecraft/' + s).json()
    uuid = j['id']
    j = get('https://sessionserver.mojang.com/session/minecraft/profile/' + uuid).json()
    value = j['properties'][0]['value']#I hope there's only ever one
    j = loads(b64decode(value).decode('UTF-8'))
    url = j['textures']['CAPE' if cape else 'SKIN']['url']
    return url[7:29], url[29:]

def handle_response(client, server):
    while True:
        data = server.recv(1024)
        if len(data) > 0:
            client.sendall(data)
        else:
            break
    server.close()

def handle_request(client):
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
    
    if 'MinecraftSkins' in message:
        url = fetch_url(message, False)
    elif 'MinecraftCloaks' in message:
        url = fetch_url(message, True)
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
    handle_response(client, server)

    client.close()

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 46653))
server.listen()

while True:
    client, addr = server.accept()
    Thread(
        target = handle_request,
        args = (client,)
    ).start()
