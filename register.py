import requests
import time

class register():
    def __init__(self, email, username, password, proxy):
        self.email = email
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
            'first_name' : '',
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
        print(send_request.cookies['csrftoken'])

def creator_handler():
    log_file = open('usernames.txt', 'a')
    password = ""
    i = 0
    while True:
        username = "" + str(i)
        email = username + "@gmail.com"
        proxy = None
        create_account = register(email, username, password, proxy)
        create_account.register_account()
        log_file.write(username + "\n")
        log_file.flush()
        print(username)
        time.sleep(60)
        i = i + 1
    log_file.close()

def main():
    creator_handler()
 
if __name__ == '__main__':
    main()