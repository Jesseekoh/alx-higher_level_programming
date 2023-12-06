#!/usr/bin/python3
""" a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

import requests
from sys import argv

if __name__ == '__main__':

    # Create a session
    session = requests.Session()
    username = argv[1]
    password = argv[2]
    # Set the username and password for authentication
    session.auth = (username, password)

    # Make a GET request to the GitHub API to get the user's information
    response = session.get('https://api.github.com/user')

    # Check if the request was successful
    if response.status_code == 200:
        # Get the user's id from the response
        user_id = response.json()['id']

        # Display the user's id
        print(f"GitHub ID: {user_id}")
    else:
        print("Failed to retrieve GitHub ID")
