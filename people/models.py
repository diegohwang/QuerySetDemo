#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals#必须放在首行
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class man(models.Model):
    name = models.CharField('姓名', max_length=128)
    age = models.CharField('年龄', max_length=128)
    email = models.TextField('邮箱', default='')
        
    def __str__(self):
        return self.name
    
class subject(models.Model):
    