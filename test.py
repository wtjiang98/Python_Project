import re

text = '''
<!doctype html>

<html><head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Amaze UI Admin index Examples</title>
    <meta name="description" content="这是一个 index 页面">
    <meta name="keywords" content="index">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="renderer" content="webkit">
    <meta http-equiv="Cache-Control" content="no-siteapp">
    <link rel="icon" type="image/png" href="assets/i/favicon.png">
    <link rel="apple-touch-icon-precomposed" href="assets/i/app-icon72x72@2x.png">
    <meta name="apple-mobile-web-app-title" content="Amaze UI">
    <link rel="stylesheet" href="assets/css/amazeui.min.css">
    <link rel="stylesheet" href="assets/css/admin.css">
    <link rel="stylesheet" href="assets/css/app.css">
</head>

<body data-type="generalComponents">


<header class="am-topbar am-topbar-inverse admin-header">
    <div class="am-topbar-brand">
        <a href="javascript:;" class="tpl-logo">
            <img src="assets/img/logo.png" alt="">
        </a>
    </div>
    <div class="am-icon-list tpl-header-nav-hover-ico am-fl am-margin-right">

    </div>

    <button class="am-topbar-btn am-topbar-toggle am-btn am-btn-sm am-btn-success am-show-sm-only" data-am-collapse="{target: '#topbar-collapse'}"><span class="am-sr-only">导航切换</span> <span class="am-icon-bars"></span></button>

    <div class="am-collapse am-topbar-collapse" id="topbar-collapse">

        <ul class="am-nav am-nav-pills am-topbar-nav am-topbar-right admin-header-list tpl-header-list">

            <li class="am-hide-sm-only"><a href="javascript:;" id="admin-fullscreen" class="tpl-header-list-link"><span class="am-icon-arrows-alt"></span> <span class="admin-fullText">开启全屏</span></a></li>

            <li class="am-dropdown" data-am-dropdown="" data-am-dropdown-toggle="">
                <a class="am-dropdown-toggle tpl-header-list-link" href="javascript:;">
                    <span class="tpl-header-list-user-nick">禁言小张</span><span class="tpl-header-list-user-ico"> <img src="assets/img/user01.png"></span>
                </a>
                <ul class="am-dropdown-content">
                    <li><a href="#"><span class="am-icon-bell-o"></span> 资料</a></li>
                    <li><a href="#"><span class="am-icon-cog"></span> 设置</a></li>
                    <li><a href="#"><span class="am-icon-power-off"></span> 退出</a></li>
                </ul>
            </li>
            <li><a href="###" class="tpl-header-list-link"><span class="am-icon-sign-out tpl-header-list-ico-out-size"></span></a></li>
        </ul>
    </div>
</header>







<div class="tpl-page-container tpl-page-header-fixed">


    <div class="tpl-left-nav tpl-left-nav-hover">
        <div class="tpl-left-nav-title">业务信息列表</div>
        <div class="tpl-left-nav-list">
            <ul class="tpl-left-nav-menu">
                <li class="tpl-left-nav-item">
                    <a href="zxbx_index.html" class="nav-link active">
                        <i class="am-icon-home"></i>
                        <span>首页</span>
                    </a>
                </li>
                <li class="tpl-left-nav-item">
                    <a href="javascript:;" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-table"></i>
                        <span>医疗基本信息</span>
                        <i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right"></i>
                    </a>
                    <ul class="tpl-left-nav-sub-menu" style="display: none;">
                        <li>
                            <a href="table-font-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>药品信息</span>
                                <i></i>
                            </a>

                            <a href="table-images-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>诊疗项目信息</span>


                            </a><a href="form-news.html">
                            <i class="am-icon-angle-right"></i>
                            <span>病种信息</span>



                        </a><a href="form-news.html">
                            <i class="am-icon-angle-right"></i>
                            <span>服务设施项目信息</span>



                        </a><a href="form-news-list.html">
                            <i class="am-icon-angle-right"></i>
                            <span>定点医疗信息</span>

                        </a>
                        </li>
                    </ul>
                </li>


                <li class="tpl-left-nav-item">
                    <a href="javascript:;" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-table"></i>
                        <span>医疗待遇计算参数维护</span>
                        <i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right"></i>
                    </a>
                    <ul class="tpl-left-nav-sub-menu" style="display: none;">
                        <li>
                            <a href="table-font-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>封顶线</span>
                                <i></i>
                            </a>

                            <a href="table-images-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>起付标准</span>


                            </a><a href="form-news.html">
                            <i class="am-icon-angle-right"></i>
                            <span>个人分段自费比例</span>



                        </a>
                        </li>
                    </ul>
                </li>

                <li class="tpl-left-nav-item">
                    <a href="javascript:;" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-table"></i>
                        <span>医疗待遇审批</span>
                        <i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right"></i>
                    </a>
                    <ul class="tpl-left-nav-sub-menu" style="display: none;">
                        <li>
                            <a href="table-font-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>药品信息</span>
                                <i></i>
                            </a>

                            <a href="table-images-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>诊疗项目信息</span>


                            </a><a href="form-news.html">
                            <i class="am-icon-angle-right"></i>
                            <span>病种信息</span>



                        </a><a href="form-news-list.html">
                            <i class="am-icon-angle-right"></i>
                            <span>定点医疗信息</span>

                        </a>
                        </li>
                    </ul>
                </li>

                <li class="tpl-left-nav-item">
                    <a href="javascript:;" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-table"></i>
                        <span>医疗中心报销</span>
                        <i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right tpl-left-nav-more-ico-rotate"></i>
                    </a>
                    <ul class="tpl-left-nav-sub-menu" style="display: block;">
                        <li>
                            <a href="zxbx_index.html">
                                <i class="am-icon-angle-right"></i>
                                <span>中心报销</span>
                                <i></i>
                            </a>

                            <a href="table-images-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>取消报销</span>




                            </a>
                        </li>
                    </ul>
                </li>

                <li class="tpl-left-nav-item">
                    <a href="javascript:;" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-table"></i>
                        <span>综合查询</span>
                        <i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right"></i>
                    </a>
                    <ul class="tpl-left-nav-sub-menu" style="display: none;">
                        <li>
                            <a href="table-font-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>医疗人员费用信息</span>
                                <i></i>
                            </a>


                        </li>
                    </ul>
                </li>

                <li class="tpl-left-nav-item">
                    <a href="javascript:;" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-table"></i>
                        <span>公共业务</span>
                        <i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right"></i>
                    </a>
                    <ul class="tpl-left-nav-sub-menu" style="display: none;">
                        <li>
                            <a href="table-font-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>单位基本信息</span>
                                <i></i>
                            </a>

                            <a href="table-images-list.html">
                                <i class="am-icon-angle-right"></i>
                                <span>个人基本信息</span>


                            </a>
                        </li>
                    </ul>
                </li>

                <li class="tpl-left-nav-item">
                    <a href="login.html" class="nav-link tpl-left-nav-link-list">
                        <i class="am-icon-key"></i>
                        <span>登录</span>

                    </a>
                </li>
            </ul>
        </div>
    </div>



    <div class="tpl-content-wrapper">
        <div class="tpl-content-page-title">医疗中心报销</div>
        <ol class="am-breadcrumb">
            <li><a href="#" class="am-icon-home">首页</a></li>
            <li><a href="zxbx_index.html">中心报销</a></li>
            <li><a href="msg_jz.html">就诊资料信息</a></li>
            <li class="am-active">录入处方明细信息</li>
        </ol>


        <div class="tpl-portlet-components">
            <div class="portlet-title">
                <div class="caption font-green bold">
                    <span class="am-icon-code"></span>录入处方明细信息
                </div>
                <div class="tpl-portlet-input tpl-fz-ml">
                    <div class="portlet-input input-small input-inline">
                        <div class="input-icon right">
                        </div>
                    </div>
                </div>
            </div>

            <div class="tpl-block ">

                <div class="am-g tpl-amazeui-form">

                    <div class="am-u-sm-12 am-u-md-9">
                        <form class="am-form am-form-horizontal">
                            <div class="am-form-group">
                                <label for="user-name" class="am-u-sm-3 am-form-label">住院号</label>
                                <div class="am-u-sm-9">
                                    <input type="text" id="user-name" placeholder="输入住院号">
                                </div>
                            </div>
                            <div class="am-form-group">
                                <label for="user-phone" class="am-u-sm-3 am-form-label">收费类别</label>
                                <div class="am-u-sm-9">
                                    <select data-am-selected="{searchBox: 1}" style="display: none;">
                                        <option value="a">甲</option>
                                        <option value="b">乙</option>
                                        <option value="o">丙</option>
                                    </select>
                                </div>
                            </div>
                            <div class="am-form-group">
                                <label for="user-email" class="am-u-sm-3 am-form-label">药品名称</label>
                                <div class="am-u-sm-9">
                                    <input type="email" id="user-email" placeholder="输入药品名称">
                                </div>
                            </div>
                            <div class="am-form-group">
                                <label for="user-weibo" class="am-u-sm-3 am-form-label">单价</label>
                                <div class="am-u-sm-9">
                                    <input type="text" id="user-weibo" placeholder="输入单价">
                                </div>
                            </div>
                            <div class="am-form-group">
                                <label for="user-weibo" class="am-u-sm-3 am-form-label">数量</label>
                                <div class="am-u-sm-9">
                                    <input type="text" id="user-weibo" placeholder="输入数量">
                                </div>
                            </div>
                            <div class="am-form-group">
                                <label for="user-weibo" class="am-u-sm-3 am-form-label">总价</label>
                                <div class="am-u-sm-9">
                                    <input type="text" id="user-weibo" placeholder="输入总价">
                                </div>
                            </div>
                            <div class="am-form-group">
                                <div class="am-u-sm-9 am-u-sm-push-3">
                                    <button type="button" class="am-btn am-btn-primary">添加</button>
                                    <a href="index.html">
                                        　　<input type="button" class="am-btn am-btn-default"  onclick="window.location.href('连接')"  value="返回">
                                    </a>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>


<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/amazeui.min.js"></script>
<script src="assets/js/app.js"></script>


</body></html>

'''

res = re.search('<div class="tpl-left-nav tpl-left-nav-hover"[\s\S]*?</li>\s*</ul>\s*</div>\s*</div>', text)

rr = re.sub('html', 'asdfasdf', text)
