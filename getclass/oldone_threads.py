import requests, time, _thread

s = requests.session()
url = 'http://edusys.hrbeu.edu.cn/jsxsd/xk/LoginToXk'
data = {
    'encoded': 'MjAxNTIwMTEyNA==%%%eXo3NzgxNTc='
}
cur = s.post(url=url, data=data)
# print(cur.text)
# print(s.cookies)

# 点击选课中心
url = 'http://edusys.hrbeu.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL'
cur = s.get(url)
# print(cur.text)
# print(s.cookies)

# 进入选课按钮 第一次
url = 'http://edusys.hrbeu.edu.cn/jsxsd/xsxk/xklc_view?jx0502zbid=24E47B01842B422EBCDB3A4A61A6D4B6'
cur = s.get(url)
# print(cur.text)
# print(s.cookies)

# 进入选课按钮 第二次
url = 'http://edusys.hrbeu.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=24E47B01842B422EBCDB3A4A61A6D4B6'
cur = s.get(url)


# print(cur.text)
# print(s.cookies)

# final

def get1():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/xxxkOper?jx0404id=201720181004724')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('系统设计', cnt)
            cnt += 1


def get2():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/xxxkOper?jx0404id=201720181004689')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('信息安全', cnt)
            cnt += 1


def get3():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/xxxkOper?jx0404id=201720181004699')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('C++', cnt)
            cnt += 1


def get4():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/xxxkOper?jx0404id=201720181004704')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('应用软件', cnt)
            cnt += 1

            
def get5():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id=201720181007469&xkzy=&trjf=')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('经济学百年', cnt)
            cnt += 1


def get6():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id=201720181007464&xkzy=&trjf=')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('创新创业领导力', cnt)
            cnt += 1


def get7():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id=201720181007497&xkzy=&trjf=')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('设计创意生活', cnt)
            cnt += 1


def get8():
    cnt = 1
    while (1):
        ans = s.get('http://edusys.hrbeu.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id=201720181007499&xkzy=&trjf=')
        ret = ans.json()
        print(ret)
        if (ret['success'] == True):
            break
        else:
            time.sleep(0.2)
            print('创造性思维与创新方法', cnt)
            cnt += 1

try:
    _thread.start_new_thread(get1, ())
    _thread.start_new_thread(get2, ())
    _thread.start_new_thread(get3, ())
    _thread.start_new_thread(get4, ())
    _thread.start_new_thread(get5, ())
    _thread.start_new_thread(get6, ())
    _thread.start_new_thread(get7, ())
    _thread.start_new_thread(get8, ())

except:
    print("wrong")

while (1):
    pass



