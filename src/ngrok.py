from pyngrok import ngrok

from src.util import get_ngrok_auth


def register_host_ip(app, _):
    auth = get_ngrok_auth()
    if auth:
        ngrok.set_auth_token(auth)
    public_url = ngrok.connect(addr=9090, port=9090, bind_tls=True)
    print(public_url)
