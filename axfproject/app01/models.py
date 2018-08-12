from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class BaseData(models.Model):
    img = models.CharField(
        max_length=255,
        verbose_name='图片链接'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='介绍名字'
    )
    trackid = models.CharField(
        max_length=100,
        verbose_name='trackid'
    )
    class Meta:
        abstract = True

class Wheel(BaseData):

    class Meta:
        db_table="axf_wheel"


class Nav(BaseData):

    class Meta:
        db_table="axf_nav"


class MustBuy(BaseData):

    class Meta:
        db_table="axf_mustbuy"


class Shop(BaseData):
    class Meta:
        db_table = "axf_shop"


class MainInfo(models.Model):
    trackid = models.CharField(
        max_length= 200
    )
    name = models.CharField(
        max_length= 200
    )
    img = models.CharField(
        max_length= 200
    )
    categoryid = models.CharField(
        max_length= 200
    )
    brandname = models.CharField(
        max_length= 200
    )
    img1 = models.CharField(
        max_length= 200
    )
    childcid1 = models.CharField(
        max_length= 200
    )
    productid1 = models.CharField(
        max_length= 200
    )
    longname1 = models.CharField(
        max_length= 200
    )
    price1 = models.CharField(
        max_length= 200
    )
    marketprice1 = models.CharField(
        max_length= 200
    )
    img2 = models.CharField(
        max_length= 200
    )
    childcid2 = models.CharField(
        max_length= 200
    )
    productid2 = models.CharField(
        max_length= 200
    )
    longname2 = models.CharField(
        max_length= 200
    )
    price2 = models.CharField(
        max_length= 200
    )
    marketprice2 = models.CharField(
        max_length= 200
    )
    img3 = models.CharField(
        max_length= 200
    )
    childcid3 = models.CharField(
        max_length= 200
    )
    productid3 = models.CharField(
        max_length= 200
    )
    longname3 = models.CharField(
        max_length= 200
    )
    price3 = models.CharField(
        max_length= 200
    )
    marketprice3 = models.CharField(
        max_length= 200
    )
    class Meta:
        db_table="axf_mainshow"

# axf_foodtypes(typeid,typename,childtypenames,typesort)
class GoodsTypes(models.Model):
    typeid = models.CharField(
        max_length=40
    )
    typename = models.CharField(
        max_length=10
    )
    childtypenames = models.CharField(
        max_length=200,
    )
    typesort = models.IntegerField()

    class Meta:
        db_table = "axf_foodtypes"


class Goods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=200
    )
    productname = models.CharField(
        max_length=200,
        null=True
    )
    productlongname = models.CharField(
        max_length=200
    )
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.BooleanField(
        default=0
    )
    specifics = models.CharField(
        max_length=20
    )
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=10
    )
    dealerid = models.CharField(
        max_length=20
    )
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    def __str__(self):
        return str(self.price)

    class Meta:
        db_table = "axf_goods"


class MyUser(AbstractUser):
    nick_name = models.CharField(
        max_length=20,
        verbose_name="昵称",
        null=True
    )
    icon = models.ImageField(
        upload_to="icons",
        verbose_name="头像"
    )
    phone = models.CharField(
        max_length=12,
        verbose_name="手机号",
        null=True
    )
    address = models.TextField(
        max_length=1000,
        verbose_name="地址",
        null=True
    )

