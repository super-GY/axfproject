from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import login
from django.core.cache import cache
from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from app01 import models
from .axf_utils import send_active_email
# Create your views here.

def home(req):
    title = "首页"
    # 轮播
    swipers = models.Wheel.objects.all()
    # 导航栏
    navs = models.Nav.objects.all()
    mustbuys = models.MustBuy.objects.all()
    shops = models.Shop.objects.all()
    maininfos = models.MainInfo.objects.all()
    shop0 = shops[0]
    data = {
        'title': title,
        'swipers': swipers,
        'mynavs': navs,
        'mustbuys': mustbuys,
        'shop0': shop0,
        'shop1_3': shops[1:3],
        'shop3_7':shops[3:7],
        'shop7_11': shops[7:],
        'maininfos': maininfos
    }
    return render(req, 'home/home.html', context=data)

def market(req):
    # g_types = models.GoodsTypes.objects.all()
    # data ={
    #     'title': '闪购',
    #     'goodstypes': g_types
    # }
    return redirect(reverse("axf:market_with_param", args=("104749", "0" ,"0")))

def market_with_param(req, param_typeid, sub_typeid, sort_type):
    # print(sort_type)
    sort_type = int(sort_type)
    g_types = models.GoodsTypes.objects.all()
    """
        0 综合排序
        1 价格最低
        2 销量优先
    """
    # 查询商品多加了一个小分类条件（childcid）
    if int(sub_typeid) == 0:
        # 处理全部分类
        goods = models.Goods.objects.filter(categoryid=param_typeid)
    else:
        goods = models.Goods.objects.filter(categoryid=param_typeid, childcid=sub_typeid)

    ZH_SORT = 0
    PRICE_SORT = 1
    SALE_SORT = 2
    if sort_type == ZH_SORT:
        pass
    elif sort_type == PRICE_SORT:
        goods = goods.order_by("price")
    else:
        goods = goods.order_by("productnum")
    print(goods)


    my_sub_types = []
    sub_cates = g_types.filter(typeid=param_typeid)
    if sub_cates.count()<=0:
        raise Exception("nothing find")
    else:
        # sub_cates = g_types.filter(typeid=param_typeid)
        # 根据类型id拿到子分类id
        sub_cates_str = sub_cates.first().childtypenames
        # 对数据进行切分处理
        sub_cates_array = sub_cates_str.split("#")
        # print(sub_cates_array)
        for i in sub_cates_array:
            tmp = i.split(":")
            my_sub_types.append(tmp)
        # print(my_sub_types)

    data = {
        'title': '闪购',
        'goodstypes': g_types,
        'selectedid': param_typeid,
        'goods': goods,
        'sub_types': my_sub_types,
        'selected_sub_type_id': sub_typeid,
        'sort_type': int(sort_type)
    }

    return render(req, 'market/market.html', data)

def cart(req):
    return render(req, 'cart/cart.html')

def mine(req):
    return render(req, 'mine/mine.html')


#注册
class RegisterAPI(View):

    def get(self, req):
        return render(req, 'user/register.html')

    def post(self, req):

        #//校验用户名是不是规则
        # //邮箱是否合法
        # //密码长度和规则 正则可以实现

        # 拿参数
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        pwd_confirm = params.get("pwd_confirm")
        email = params.get("email")
        # print(params)

        # 校验邮箱的合法性 正则可以实现

        #拿图片
        icon = req.FILES.get("icon")
        # print(icon)
        # 简单的用户校验
        user_count = models.MyUser.objects.filter(username=u_name).count()
        if user_count != 0:
            return HttpResponse("该用户已存在")

        if pwd and pwd_confirm and pwd==pwd_confirm:
            # 新建用户
            user = models.MyUser.objects.create_user(
                username=u_name,
                email=email,
                password=pwd,
                icon=icon,
                is_active=False)
            # f发送验证邮件
            send_active_email(email)
            # 进入登陆页
            return redirect(reverse("axf:login"))
        else:
            return HttpResponse("shibai")


class LoginApi(View):
    def get(self, req):
        return render(req, 'user/login.html' )
    def post(self,req):
        param=QueryDict(req.body)
        u_name=param.get("u_name")
        pwd=param.get('pwd')
        if pwd and u_name and len(pwd)>2 and (len(u_name)>0 and len(u_name)<10):
            user = authenticate(username=u_name, password=pwd)
            if user:
                login(req, user)
                return render(reverse("axf:mine"))
            else:
                return redirect(reverse("axf:login"))
        else:
            return redirect(reverse("axf:login"))


def active(req, token):
    email = cache.get(token)
    if email:
        user = models.MyUser.objects.filter(email=email)
        if user.count() == 1:
            user.is_active = True
            return redirect(reverse('axf:mine'))
        else:
            return HttpResponse("<h1>密码失效</h1>")
    else:
        return HttpResponse("<h1>密码失效</h1>")