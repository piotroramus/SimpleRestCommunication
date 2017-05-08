import argparse
import requests

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1', help='IP address of the listening server')
    parser.add_argument('--port', default='5000', help='port of the listening server')
    args = parser.parse_args()
    host = args.host
    port = args.port

    url = "http://{}:{}/hello".format(host, port)

    try:
        r = requests.get(url)
        print(r.content)
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server...")
