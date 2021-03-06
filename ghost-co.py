import string
import threading
import random
import requests
import platform

from colorama import Fore, init

if platform.system() != 'Linux':
    init(convert=True)

def save_url(content):
    with open('./ghostbin/hits.txt', 'a+') as f:
        f.write(content + '\n')


def check_urls():
    while True:
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))
        r = requests.get(f'https://ghostbin.co/paste/{code}')
        if r.status_code == 404:
            print(f'[{Fore.RED}404{Fore.RESET}] => {r.url}')
        else:
            save_url(r.url)
            print(f'[{Fore.GREEN}{r.status_code}{Fore.RESET}] => {r.url}')


def main(threads):
    if threading.active_count() <= threads:
        t = threading.Thread(target=check_urls)
        t.start()


thread = int(input("How many threads: "))
main(thread)
