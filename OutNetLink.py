#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests


# '''
# 在官网直接登录的URL貌似不好使，第一个是/6的一个什么post
# 在进入注销后能得到一个简单的登录窗口，直接带data用post即可登录
# 带cookies会报Unicode错，大概是cookies里有非法字符，http head貌似
# 只支持Latin-1字符集
# '''

def getConn():
    s = requests.session()
    url = 'https://ssl.hrbeu.edu.cn/por/login_psw.csp'
    mycoo = {'_gscu_2051300436': "999075300q8tx216", '_gscbrs_2051300436': "1",
             'collection': "{page_state:'started',auto_login_count:0}", 'haveLogin': "0", 'LoginMode': "2",
             'websvr_cookie': "1499925034904001", 'VisitTimes': "0", '_gscs_2051300436': "t99925455wezbnl16|pv:2",
             'g_LoginPage': "login_psw", 'TWFID': "44c0322a3bd7fa46"}

    data = {'svpn_name': "2015201108", 'svpn_password': "jwt19980331", 'svpn_rand_code': ""}

    res = s.post(url=url, data=data, cookies=mycoo, verify=False)
    return s

    # 以下为测试用外网登录教务处
    # url = 'https://ssl.hrbeu.edu.cn/web/1/http/0/jw.hrbeu.edu.cn/'
    # cur = s.get(url=url)
    # print(cur, cur.text)

if __name__ == '__main__':
    getConn()
