import os
import os.path
import re


def line_prepender(filename, line):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        # print(content)
        res = re.search('(?i)<!doctype html>', content)
        if res is None:
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)


def go_add():
    rootdir = r'D:\Dalian_CUR\amz_4_baf'
    for parent, dirnames, filenames in os.walk(rootdir):
        # case 2
        for filename in filenames:
            url = os.path.join(parent, filename)
            if re.search('html', filename):
                line_prepender(url, '<!doctype html>')


def daohang(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        # res = re.search('<div class="tpl-left-nav tpl-left-nav-hover"[\s\S]*?</li>\s*</ul>\s*</div>\s*</div>', content)
        # if res is not None:
        #     content = re.sub('<div class="tpl-left-nav tpl-left-nav-hover"[\s\S]*?</li>\s*</ul>\s*</div>\s*</div>',
        #                      lines, content)



        content = re.sub('<a href=[\s\S]{,188}<span>个人基本信息', '''<a href="basical_people.html">
                                <i class="am-icon-angle-right"></i>
                                <span>个人基本信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>单位基本信息', '''<a href="basical_institutions.html">
                                <i class="am-icon-angle-right"></i>
                                <span>单位基本信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>医疗人员费用信息', '''<a href="annual_baoxiao.html">
                                <i class="am-icon-angle-right"></i>
                                <span>医疗人员费用信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>取消报销', '''<a href="cancel.html">
                                <i class="am-icon-angle-right"></i>
                                <span>取消报销''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>中心报销', '''<a href="zxbx_index.html">
                                <i class="am-icon-angle-right"></i>
                                <span>中心报销''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>个人分段自费比例', '''<a href="个人分段自费比例查询.html">
                            <i class="am-icon-angle-right"></i>
                            <span>个人分段自费比例''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>起付标准', '''<a href="起付标准信息查询.html">
                                <i class="am-icon-angle-right"></i>
                                <span>起付标准''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>封顶线', '''<a href="封顶线查询.html">
                                <i class="am-icon-angle-right"></i>
                                <span>封顶线''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>定点医疗信息', '''<a href="定点医疗机构信息查询.html">
                            <i class="am-icon-angle-right"></i>
                            <span>定点医疗信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>服务设施项目信息', '''<a href="服务设施项目查询.html">
                            <i class="am-icon-angle-right"></i>
                            <span>服务设施项目信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>病种信息', '''<a href="病种信息查询.html">
                            <i class="am-icon-angle-right"></i>
                            <span>病种信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>诊疗项目信息', '''<a href="诊疗项目查询.html">
                                <i class="am-icon-angle-right"></i>
                                <span>诊疗项目信息''', content)

        content = re.sub('<a href=[\s\S]{,188}<span>药品信息', '''<a href="药品信息查询.html">
                                <i class="am-icon-angle-right"></i>
                                <span>药品信息''', content)

        # res = re.search('<li class="tpl-left-nav-item">[\s\S]{,200}<span>登录</span>[\s\S]*?</li>', content)
        # print(res.group())
        content = re.sub('<li class="tpl-left-nav-item">[\s\S]{,200}<span>登录</span>[\s\S]*?</li>', ' ', content)
        # print(content)
        # while 1:
        #     pass
        f.seek(0, 0)
        f.write(content)


def go_daohang():
    rootdir = r'D:\Dalian_CUR\amz_4_baf'
    for parent, dirnames, filenames in os.walk(rootdir):
        # case 2
        for filename in filenames:
            url = os.path.join(parent, filename)
            if re.search('html', filename):
                daohang(url)


if __name__ == '__main__':
    go_daohang()
