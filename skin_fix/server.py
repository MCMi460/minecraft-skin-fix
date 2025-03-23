from . import Flask, getLogger, Response, get
from .proxy import Proxy

# Init Flask server
app = Flask(__name__)
getLogger('werkzeug').disabled = True
app.logger.disabled = True

@app.route('/<path:path>')
def app_path(path):
    path = '/' + path
    if 'MinecraftSkins' in path:
        url = Proxy.fetch_url(path, False)
    elif 'MinecraftCloaks' in path:
        url = Proxy.fetch_url(path, True)
    else:
        return Response(status = 500)
    return get('http://' + ''.join(url)).content

class Server:
    def start(*args):
        app.run(host = '0.0.0.0', port = 80)
