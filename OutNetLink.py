import requests


# noinspection PyArgumentList



def getConn():
    global res
    s = requests.session()
    url = 'https://ssl.hrbeu.edu.cn/073820d43bd7fa47/web/1/http/0/portal.hrbeu.edu.cn/web/guest/6'
    mycoo = dict(_gscu_2051300436="62065139tjc3ej98", _ga="GA1.3.1644293419.1473595787",
                 _gscs_2051300436="99866591z34jxk12|pv:3", _gscbrs_2051300436="1",
                 collection="{page_state:'started',auto_lo…,scacheUseable:0,AppCount:0}", haveLogin="1", LoginMode="2",
                 websvr_cookie="1499866353265744", VisitTimes="0", g_LoginPage="0", TWFID="073820d43bd7fa47")
    data = dict(
        _58_login="2015201108", _58_password="jwt19980331", _58_struts_action="/login/login", p_p_col_count=
        "2", p_p_col_id="column-2", p_p_id="58", p_p_lifecycle="1", p_p_mode="view", p_p_state=
        "normal", saveLastPath="0",
    )
    try:
        res = s.post(url=url, data=data, cookies=mycoo)
    except:
        print('wrong')
        print(res.status_code, res.text)


if __name__ == '__main__':
    getConn()
