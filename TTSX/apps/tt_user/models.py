from django.db import models
#不懂？？？？？？
from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel

# Create your models here.
#用户类
class User(AbstractUser,BaseModel):
    class Meta:  # ttsx-->dailyfresh-->df
        db_table = 'tt_user'

#地区类
class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'tt_area'

#订单类
class Address(BaseModel):
    #接收者
    receiver = models.CharField(max_length=10)
    #省
    province = models.ForeignKey('AreaInfo', related_name='province')
    #城市
    city = models.ForeignKey('AreaInfo', related_name='city')
    #区域；地方；行政区
    district = models.ForeignKey('AreaInfo', related_name='district')
    #（详细）地址
    addr = models.CharField(max_length=20)
    #（邮政）编码
    code = models.CharField(max_length=6)
    #电话号码
    phone_number = models.CharField(max_length=11)
    #是否送达？？
    isDefault = models.BooleanField(default=0)
    #用户
    user = models.ForeignKey('User')

    class Meta:
        db_table = 'df_address'
        # address==>addr.provice
        # area==>area.addressinfo_set