#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen

req = Request("https://alx-intranet.hbtn.io/status")
with urlopen(req) as response:
    the_page = response.read()

    print(f"Body response:\n\t- type: {type(the_page)}")
    print(f"\t- content: {the_page}")
    print(f"\t- utf8 content: {the_page.decode('utf-8')}")
