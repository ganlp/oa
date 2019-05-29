from django.db import models

# Create your models here.
class Dept(models.Model):
    """部门类"""
    no=models.IntergerField(primary_key=True,db_column="dbn",verbose_name="部门编号")
    name=models.CharField(max_length=20,db_column='dname',verbose_name="部门名称")
    location=models.CharField(max_length=10,db_column="dloc",verbose_name="部门所在地")

    class Meta:
        db_table='tb_dept'


 class Emp(models.Model):
    """员工类"""
    no=models.IntergerField(primary_key=True,db_column='eno',verbose_name="员工编号")
    name=models.Char
