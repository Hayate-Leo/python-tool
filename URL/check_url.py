import requests


def check_request(url):
    request = requests.get(url)
    return request.status_code

if __name__ == '__main__':
    print(check_request('http://www.example.com/thy'))