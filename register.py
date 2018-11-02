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
    log_file = open('accounts.txt', 'a')
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

def creator_handler_proxies(sleep, proxyfile):
    log_file = open('accounts.txt', 'a')
    with open(proxyfile, "r") as proxy_file:
        proxies = proxy_file.readlines()
    proxies = [x.strip() for x in proxies]
    i = 0
    while True:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        name = names.get_full_name()
        email = username + "@gmail.com"
        proxy = proxies[i]
        create_account = register(email, name, username, password, proxy)
        create_account.register_account()
        log_file.write(name + " : " + "@" + username + " : " + password +  "\n")
        log_file.flush()
        print("Name: " + name)
        print("Email:" + email)
        print("Username: @" + username)
        print("Password: " + password)
        print("Speed: " + str(sleep) + " milliseconds.")
        print("Proxy: " + proxies[i])
        print("------------------------------")
        time.sleep(sleep)
        i = i + 1
    log_file.close()

def main():
    print("Instagram Account Creator")
    print("Press ctrl-z to quit at anytime.")
    print("Are you using proxies? (y/n)")
    if (input() == "y"):
        print("Please enter a delay in milliseconds: ")
        user_speed = input()
        try:
            handler_speed = float(user_speed)
            creator_handler_proxies(handler_speed, 'proxies.txt')
        except ValueError:
            print("Not a float value.")
            main()
    elif (input() == "n"):
        print("Please enter a delay in milliseconds: ")
        user_speed = input()
        try:
            handler_speed = float(user_speed)
            creator_handler(handler_speed)
        except ValueError:
            print("Not a float value.")
            main()
    else:
        main()
 
if __name__ == '__main__':
    main()
