import requests

if __name__ == '__main__':

    url = "http://127.0.0.1:5000/hello"

    try:
        r = requests.get(url)
        print(r.content)
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server...")
