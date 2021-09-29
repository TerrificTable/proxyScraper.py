import requests
import json
import os
from colorama import Fore, Style

banner = f'''
{Fore.CYAN} _____                   {Fore.GREEN} _____                                
{Fore.CYAN}| ___ \                  {Fore.GREEN}/  ___|                               
{Fore.CYAN}| |_/ / __ _____  ___   _{Fore.GREEN}\ `--.  ___ _ __ __ _ _ __   ___ _ __ 
{Fore.CYAN}|  __/ '__/ _ \ \/ / | | |{Fore.GREEN}`--. \/ __| '__/ _` | '_ \ / _ \ '__|
{Fore.CYAN}| |  | | | (_) >  <| |_| {Fore.GREEN}/\__/ / (__| | | (_| | |_) |  __/ |   
{Fore.CYAN}\_|  |_|  \___/_/\_\\__,  {Fore.GREEN}\____/ \___|_|  \__,_| .__/ \___|_|   
{Fore.CYAN}                     __/ |{Fore.GREEN}                    | |              
{Fore.CYAN}                    |___/ {Fore.GREEN}                    |_|              {Style.RESET_ALL}'''

err = f"[{Fore.RED}-{Style.RESET_ALL}]"
out = f"[{Fore.GREEN}:{Style.RESET_ALL}]"
inf = f"[{Fore.YELLOW}i{Style.RESET_ALL}]"
inp = f"[{Fore.MAGENTA}>{Style.RESET_ALL}] $ "
log = f"[{Fore.CYAN}={Style.RESET_ALL}]"
finish = f"press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit"

def get_proxy():
    global proxys
    r = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/json/proxies-http%2Bhttps-beautify.json")

    f = open("./proxys.json", "w")
    f.write(r.text)
    f.close()

proxyHttp = ""
proxyHttps = ""

def load_proxy():
    global proxysHttp, proxysHttps
    f = open("./proxys.json", "r")
    proxys = json.load(f)
    proxysHttp = proxys.get("http")
    proxysHttps = proxys.get("https")
    f.close()


def screen():
    os.system("cls; clear")
    os.system("title [Terrific's ProxyScraper - Menu]")
    os.system(f'mode 110,30')
    print(banner)
    print(f'''{Fore.MAGENTA}
    [x]================================[x]
     ║  {Fore.RED}[1]{Style.RESET_ALL}{Fore.MAGENTA}  =>  {Fore.WHITE}Update/Get ProxyList{Style.RESET_ALL}{Fore.MAGENTA}   ║
     ║  {Fore.RED}[2]{Style.RESET_ALL}{Fore.MAGENTA}  =>  {Fore.WHITE}Write List as json{Style.RESET_ALL}{Fore.MAGENTA}     ║
     ║  {Fore.RED}[3]{Style.RESET_ALL}{Fore.MAGENTA}  =>  {Fore.WHITE}Exit{Style.RESET_ALL}{Fore.MAGENTA}                   ║
    [x]================================[x]{Style.RESET_ALL}
    ''')
    choise = input(f"{inp} ")

    if str(choise) == "1":
        os.system("title [Terrific's ProxyScraper - Get Proxys]")
        print(f"{inf} Getting Proxys")
        proxys = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/json/proxies-http%2Bhttps-beautify.json")
        get_proxy()
        print(f"{inf} Got {len(proxys.text)} Proxys, press {Fore.YELLOW}[ENTER]{Style.RESET_ALL} to return to menu"); input(); screen()
    
    elif str(choise) == "2":
        os.system("title [Terrific's ProxyScraper - Write Proxys]")
        print(f"{inf} Writing Proxys")
        load_proxy()
        print(f"{inf} Wrote Proxys to List {Fore.GREEN}(./proxys.json){Style.RESET_ALL}, press {Fore.YELLOW}[ENTER]{Style.RESET_ALL} to return to menu"); input(); screen()

    else:
        exit()
screen()
