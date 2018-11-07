"""
Author: Tyler DeGennaro
Date: 11/5/18
creator.py

This is the creator module. The creator module inititates a web session for the creation of the accounts.
A JSON response is returned by the register account method, which is used to determine in the handler class,
if an account is successfully created or not.
"""

# Library imports
import requests
import json

# Account creator class
class Account_Creator():

    # Constructor
    def __init__(self, email, name, username, password, proxy):
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        self.register_url = 'https://www.instagram.com/accounts/web_create_ajax/'
        self.referer_url = 'https://www.instagram.com/'
        self.proxy = proxy
        self.post_data = {
            'email' : self.email,
            'password' : self.password,
            'username' : self.username,
            'first_name' : self.name,
            'seamless_login_enabled' : '1',
            'tos_version' : 'row',
            'opt_into_one_tap' : 'false'
        }

    # Register account method
    def register_account(self):
        session = requests.Session()
        try:
            start_session = session.get(
                self.register_url, 
                proxies={'http' : self.proxy, 'https' : self.proxy}
            )
            session.headers.update({
                'referer' : self.referer_url,
                'x-csrftoken' : start_session.cookies['csrftoken']
            })
            send_request = session.post(self.register_url,
            data=self.post_data, 
            allow_redirects=True, 
            proxies={'http': self.proxy, 'https': self.proxy}
            )
            session.headers.update({'x-csrftoken' : start_session.cookies['csrftoken']})
            response_text = send_request.text
            response_json = json.loads(response_text)
        except requests.exceptions.ProxyError as e:
            print(e)
            print("Couldn't connect to proxy.")
        return(response_json)
