#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    result = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:\n\t- type: {type(result.text)}')
    print(f'\t- content: {result.text}')
