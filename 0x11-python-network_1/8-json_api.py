#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as
a parameter."""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    res = post(URL, data)

    res_type = res.headers['content-type']

    if res_type == 'application/json':
        result = res.json()
        d_id = result.get('id')
        name = result.get('name')
        if d_id is not None and name:
            print("[{}] {}".format(d_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
