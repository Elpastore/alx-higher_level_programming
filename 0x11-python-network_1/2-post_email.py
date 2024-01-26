#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL
"""
from urllib.request import parse, Request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        result = response.read()
        header = result.decode('utf-8')
        print(header)
