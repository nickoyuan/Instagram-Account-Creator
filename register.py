import requests
import time
import random
import string
import names

class register():
    def __init__(self, email, name, username, password, proxy):
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        self.register_url = 'https://www.instagram.com/accounts/web_create_ajax/'
        self.referer_url = 'https://www.instagram.com/'
        self.proxy = None
        self.post_data = {
            'email' : self.email,
            'password' : self.password,
            'username' : self.username,
            'first_name' : self.name,
            'seamless_login_enabled' : '1',
            'tos_version' : 'row',
            'opt_into_one_tap' : 'false'
        }
        self.session = requests.Session()

    def register_account(self):
        start_session = self.session.get(
            self.register_url, 
            proxies={'http' : self.proxy, 'https' : self.proxy}
        )
        self.session.headers.update({
            'referer' : self.referer_url,
            'x-csrftoken' : start_session.cookies['csrftoken']
        })
        send_request = self.session.post(self.register_url,
        data=self.post_data, 
        allow_redirects=True, 
        proxies={'http': self.proxy, 'https': self.proxy}
        )
        self.session.headers.update({'x-csrftoken' : start_session.cookies['csrftoken']})
        print(send_request.text)
        print("------------------------------")

def creator_handler(sleep):
    log_file = open('usernames.txt', 'a')
    while True:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        name = names.get_full_name()
        email = username + "@gmail.com"
        proxy = None
        create_account = register(email, name, username, password, proxy)
        create_account.register_account()
        log_file.write(name + " : " + "@" + username + " : " + password +  "\n")
        log_file.flush()
        print("Name: " + name)
        print("Email:" + email)
        print("Username: @" + username)
        print("Password: " + password)
        print("Speed: " + str(sleep) + " milliseconds.")
        print("------------------------------")
        time.sleep(sleep)
    log_file.close()

def main():
    print("Instagram Account Creator")
    print("To quit at any time, press ctrl-z at anytime.")
    user_speed = input("Please enter a delay in milliseconds: ")

    try:
        handler_speed = float(user_speed)
        creator_handler(handler_speed)
    except ValueError:
        print("Not a float value.")
        main()
 
if __name__ == '__main__':
    main()
