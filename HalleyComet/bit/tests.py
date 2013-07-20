#-*-coding:utf8-*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
<<<<<<< HEAD
from bit.models import Url
from bit.def_url import short_to_long, long_to_short
from django.utils import unittest
from django.test.client import Client 

class Web_Test(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/index/")
        self.assertEqual(response.status_code, 200)
    
class Url_Test(TestCase):            
    def setUp(self):
        '''
            创建数据对象
        '''
        Url.objects.create(long_url="http://www.baidu.com", short_url="aaaaab")
        Url.objects.create(long_url="http://www.google.com", short_url="aaaaac")

    def test_long_to_short(self):
        '''
            测试长url变为短的url
        '''
        long_url2 = "https://travis-ci.org/profile"
        long_url3 = "http://www.baidu.com/s?wd=sfdg+&rsv_bp=0&ch=&tn=monline_5_dg&bar=&rsv_spt=3&ie=utf-8&rsv_sug3=3&rsv_sug=0&rsv_sug4=418&rsv_sug1=2&inputT=1047"
        self.assertEqual(long_to_short(long_url2), "aaaaad")
        self.assertEqual(long_to_short(long_url3), "aaaaae")
    
    def test_long_to_short_again(self):
        '''    
            测试相同url的缩短；
            测试有无http对相同url的缩短没有影响
        '''    
        long_url = "http://tieba.baidu.com"
        long_url1 = "http://tieba.baidu.com"
        long_url2 = "tieba.baidu.com"    
        self.assertEqual(long_to_short(long_url), "aaaaad")
        self.assertEqual(long_to_short(long_url1), "aaaaad")
        self.assertEqual(long_to_short(long_url2), "aaaaad")


    def test_short_to_long(self):
        short_url = "aaaaab"
        short_url2 = "aaaaac"
        long_url = "http://tieba.baidu.com"
        short_url3 = long_to_short(long_url) 
        self.assertEqual(short_to_long(short_url), "http://www.baidu.com")
        self.assertEqual(short_to_long(short_url2), "http://www.google.com")
        self.assertEqual(short_to_long(short_url3), "http://tieba.baidu.com")


