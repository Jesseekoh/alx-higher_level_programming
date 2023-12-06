#!/usr/bin/python3
""" a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""


if __name__ == "__main__":
    from sys import argv
    import requests
    auth = (argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
