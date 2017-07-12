
import requests, re, time
#from time import strftime,gmtime
# 以后要记住！cookies是dict！！！

cnt = 0
while 1:
    data = {
        'WebUserNO': "2015201108",
        'Password': 'jwt19980331',
        'Agnomen': '2573',
        'submit.x': "26",
        'submit.y': "9",
        'applicant': "ACTIONQUERYSTUDENTSCORE"
    }
    url = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS'
    co9937 = 'ZlZh5PJcFhDp7Cfpy2MtTF6y3pyc54WqQpj9Qp3hqnkyflmGDkJg'
    mycoo = {
        'JSESSIONID': co9937
    }
    s = requests.session()
    cur = s.post(url=url, data=data, cookies=mycoo)
    cnt = cnt + 1
    print(cnt, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    if re.search('请输入正确的附加码', cur.text) is not None:
        break
    time.sleep(1)

