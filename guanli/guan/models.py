#coding:utf8
from django.db import models

# Create your models here.

class guan(models.Model):
    num = models.IntegerField("房间号码",unique=True)
    tex = models.ForeignKey('tex',verbose_name='房型')
    ceng = models.ForeignKey("ceng",verbose_name='楼层')
    zhuangtai = models.ForeignKey("zhuangtai",verbose_name="房间状态")
    jiage = models.IntegerField('房间价格')
    class Meta:
        verbose_name="酒店管理"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return str(self.num)

class tex(models.Model):
    choose=(
        (u'单人房',u'单人房'),
        (u'普通大床房',u'普通大床房'),
        (u'豪华大床房',u'豪华大床房'),
        (u'商务双床房',u'商务双床房'),
        )
    name =models.CharField(choices=choose,max_length=40)
    def __unicode__(self):
        return self.name

class ceng(models.Model):
    choose1 =(
        (u"1",u"1"),
        (u"2",u"2"),
        (u"3",u"3"),
        (u"4",u"4"),
    )
    name = models.CharField(choices=choose1,max_length=40)
    def __unicode__(self):
        return self.name
class zhuangtai(models.Model):
     choose2 = (
        (u"住净",u"住净"),
        (u"空净",u"空净"),
        (u"空脏",u"空脏"),
        (u"住脏",u"住脏"),
    )
     name = models.CharField(choices=choose2,max_length=40)
     def __unicode__(self):
        return self.name

