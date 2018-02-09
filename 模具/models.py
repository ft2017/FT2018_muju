from django.db import models

# Create your models here.
class Muju(models.Model):
    muju_wo = models.CharField('模具维修工单',max_length=50, default='.')
    muju_date = models.DateField('AMRT300日期')
    muju_empe = models.CharField('维修人员',max_length=50, default='.')
    muju_source_code = models.CharField('资源编号',max_length=50, default='.')
    muju_source_code_name = models.CharField('资源名称',max_length=50, default='.')
    muju_plan_date = models.DateField('模具预计完成日',null=True, blank=True)
    muju_seq = models.CharField('项次',max_length=10, default='.')
    muju_Reason = models.CharField('报修原因',max_length=1000, default='.')
    def __str__(self):
        return self.muju_wo

class Muju_date111(models.Model):
    Muju = models.ForeignKey(Muju, on_delete=models.CASCADE)
    muju_date1 = models.DateField('拆模计划日期', null=True,blank=True,default=' ')
    muju_date2 = models.DateField('拆模实际日期',null=True, blank=True)
    muju_date3 = models.DateField('易损与材料制作计划',null=True, blank=True)
    muju_date4 = models.DateField('易损与材料制作实际',null=True, blank=True)
    muju_date5 = models.DateField('线割计划日期',null=True, blank=True)
    muju_date6 = models.DateField('线割实际日期',null=True, blank=True)
    muju_date7 = models.DateField('烧焊计划日期',null=True, blank=True)
    muju_date8 = models.DateField('烧焊实际日期',null=True, blank=True)
    muju_date9 = models.DateField('CNC计划日期',null=True, blank=True)
    muju_date10 = models.DateField('CNC实际日期',null=True, blank=True)
    muju_date11 = models.DateField('放电计划日期',null=True, blank=True)
    muju_date12 = models.DateField('放电实际日期',null=True, blank=True)
    muju_date13 = models.DateField('抛光计划日期',null=True, blank=True)
    muju_date14 = models.DateField('抛光实际日期',null=True, blank=True)
    muju_date15 = models.DateField('组立计划日期',null=True, blank=True)
    muju_date16 = models.DateField('组立实际日期',null=True, blank=True)
    muju_date17 = models.DateField('其他计划日期',null=True, blank=True)
    muju_date18 = models.DateField('其他实际日期',null=True, blank=True)
    muju_date19 = models.DateField('备注',null=True, blank=True)
    muju_date20 = models.DateField('维修瓶颈工序',null=True, blank=True)
    muju_date21 = models.DateField('实际完成日期',null=True, blank=True)
    def __str__(self):
        return self.Muju


        