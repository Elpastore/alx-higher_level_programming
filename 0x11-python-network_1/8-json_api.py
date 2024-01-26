#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == '__main__':

    letter = "" if len(argv) < 2 else argv[1]
    value = {"q": letter}

    req = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        result = req.json()
        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
