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


def go_sub(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        content = re.sub('- More Templates', '', content)
        f.seek(0, 0)
        f.write(content)


def checklink(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        res = re.search('取消报销', content)
        if res is None:
            print(filename)


def search(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        res = re.search(
            '<a href="javascript:;" id="admin-fullscreen" class="tpl-header-list-link"><span class="am-icon-arrows-alt"></span> <span class="admin-fullText">开启全屏</span></a>',
            content)
        if res is not None:
            print(filename)


def add(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        prefix = '''<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
'''
        newname = re.sub('html', 'jsp', filename)
        # print(newname)
        with open(newname, 'w+', encoding='utf-8') as newf:
            newcontent = prefix + '\r\n' + content
            newf.write(newcontent)


def merge(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        content = re.sub('<i class="am-icon-search"></i>', '                                            ', content)
        f.seek(0, 0)
        f.write(content)


def forfile():
    global rootdir
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            url = os.path.join(parent, filename)
            if re.search('html', filename):
                add(url)


rootdir = r'D:\Dalian_CUR\CUR\amz_4_baf'

# f.seek(0, os.SEEK_CUR) 从后面append


if __name__ == '__main__':
    forfile()
