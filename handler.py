"""
Author: Tyler DeGennaro
Date: 11/5/18
handler.py

This is the main module. The handler module inititates the creation of the accounts, 
and reading and writing to .txt files.
"""


# Library imports
from creator import Account_Creator
import time
import random
import string
import names

# Handler class
class Handler():
    
    # Constructor
    def __init__(self, proxy_file):
        self.proxy_file = proxy_file
    
    # Write to file method
    def writer(self, delay, proxy):
        account_file = open('accounts.txt', 'a')
        while True:
            i = 0
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            name = first_name + " " + last_name
            username = first_name +  last_name + str(random.randint(100,999)) + first_name
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            email = username + "@gmail.com"
            for _ in range(len(proxy)):
                Create_Account = Account_Creator(email, name, username, password, proxy[i])
                try:
                    response = Create_Account.register_account()
                    print(response)
                    if(response['account_created'] == True):
                        account_file.write("Email: " + email + '\n')
                        account_file.write("Username: @" + username + '\n')
                        account_file.write("Password: " + password + '\n')
                        account_file.write(" " + '\n')
                        account_file.flush()
                        print("------------------------------")
                        print("Name: " + name)
                        print("Email:" + email)
                        print("Username: @" + username)
                        print("Password: " + password)
                        print("Proxy: " + str(proxy[i]))
                        print("Speed: " + str(delay) + " milliseconds.")
                        print("------------------------------")
                    elif(response['account_created'] == False or response['message']['status'] == 'fail'):
                        print("------------------------------")
                        print("IP address has been flagged.")
                        print("Please wait awhile, or use a different proxy.")
                        print("Proxy: " + str(proxy[i]))
                        print("Speed: " + str(delay) + " milliseconds.")
                        print("------------------------------")
                    time.sleep(delay)
                    i = i + 1
                    print("Attempt: " + str(i))
                except UnboundLocalError as e:
                    print("Failed to load JSON response.")
                    print(e)
                    break
        account_file.close()
                
    # Handler method
    def start_handler(self, proxy, delay):
        try:
            if(proxy != None):
                self.writer(delay, proxy)
            else:
                self.writer(delay, None)
        except UnboundLocalError as e:
            print("Failed to load JSON response.")
            print(e)

# Main method
def main():
    print("Are you using proxies? y/n: ")
    proxy_input = input()
    print("Enter a delay in milliseconds: ")
    delay_input = float(input())
    if(proxy_input.lower() == 'y'):
        Account_Handler = Handler("proxies.txt")
        with open(Account_Handler.proxy_file, 'r') as proxy_file:
            proxies = proxy_file.readlines()
        proxies = [line.strip() for line in proxies]
        Account_Handler.start_handler(proxies, delay_input)
    elif(proxy_input.lower() == 'n'):
        Account_Handler = Handler(None)
        Account_Handler.start_handler(None, delay_input)
    elif(proxy_input.lower() != 'y' and 'n'):
        print("You did not enter a valid command.")
        main()

# Main module
if __name__ == "__main__":
    main()
