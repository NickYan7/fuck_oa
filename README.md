## _Fuck_OA_ 🚀

### 🌍 _Description_

Fuck_OA 是一个粗糙的 OA 系统扫描器，由 Nick Yan 和 Yoga7xm 于 2020 年春天在家百无聊赖时开发，目的是为了学习和熟练 python 的高并发和代码基础，所以代码会有些不专业和粗糙的地方，欢迎批评指正。

如果这个项目有帮助到你，希望可以给我们一个 star :)

Yoga7xm: https://yoga7xm.top

Nick Yan: http://www.naykcin.top

**声明：代码仅供安全研究，请勿用做非法用途！**



### 📍 _fanwei_oa_RCE_

`/weaver/bsh.servlet.BshServlet` 存在 BeanShell 组件开放未授权访问，攻击者调用 BeanShell 组件接口可直接在目标服务器上执行任意命令。



### 📍 _tongda_oa_RCE_

`/ispirit/interface/gateway.php` 存在文件包含，且所有的访问记录会被记录在 `oa.access.log` 日志文件下。



### 📍 _tongda_oa_fake_user_

服务端只取了 `uid` 作为用户身份鉴别，由于 `uid` 是整形递增 ID，从而可以登录指定 `uid` 的用户（admin 的默认 `uid` 为 1）。

访问 `/general/login_code.php` ，生成一个二维码，`codeuid` 作为这个二维码的凭证，然后通过循环请求 `/login_code_check.php` ，将 `codeuid` 和 `uid` 两个参数发送到服务端，即可拿到 `phpsessionid` 完成伪造任意用户登录。

将 `phpsessid` 放到 `cookie` 里访问 `/general` 即可。



### 📍 _tongda_oa_fake_user_aio_

上一个漏洞的高并发版本，由 Yoga7xm 编写，速度很快且支持变量共享。

需要安装第三方库：

```python
pip install aiohttp
pip install asyncio
pip install aiomultiprocess
```



### 📍 _tongda_oa_upload_fi_

这里利用了一个文件上传 + 文件包含。

文件上传接口： `/ispirit/im/upload.php` ，文件包含漏洞触发点： `/ispirit/interface/gateway.php` 。（文件默认被保存在 `/general/../../attach/im` 目录下）



### 📍 _tongda_oa_upload_fi_aio_

上一个漏洞的高并发版本，主要利用 `aiohttp` + `asyncio` 两个库实现，支持批量检测。速度很理想，6000 多个 IP 跑了 100 秒左右，但是对于代理服务器的速度有一定要求。

需要安装第三方库：

```python
pip install aiohttp
pip install asyncio
pip install aiomultiprocess
```

