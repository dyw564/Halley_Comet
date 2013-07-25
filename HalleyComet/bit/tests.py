"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bit.models import Url
from bit.def_url import short_to_long, long_to_short

class SimpleTest(TestCase):
    def test_basic_addtion(self):
        self.assertEqual(1 + 1, 2)
   

    def setUp(self):
        Url.objects.create(long_url="http://www.baidu.com", short_url="localhost/aaaaab")
        Url.objects.create(long_url="http://www.google.com", short_url="localhost/aaaaac")

    def test_long_to_short(self):
        long_url = "www.baidu.com"
        long_url2 = "https://travis-ci.org/profile"
        long_url3 = "http://www.baidu.com/s?wd=sfdg+&rsv_bp=0&ch=&tn=monline_5_dg&bar=&rsv_spt=3&ie=utf-8&rsv_sug3=3&rsv_sug=0&rsv_sug4=418&rsv_sug1=2&inputT=1047"
        long_url_get = Url.objects.filter(long_url="www.baidu.com")
        self.assertEqual(long_to_short(long_url), "localhost/aaaaab")
        self.assertEqual(long_to_short(long_url2), "localhost/aaaaad")
        self.assertEqual(long_to_short(long_url3), "localhost/aaaaae")

    def test_short_to_long(self):
        short_hash = "aaaaab"
        short_hash2 = "aaaaac"
        self.assertEqual(short_to_long(short_hash), "http://www.baidu.com")
        self.assertEqual(short_to_long(short_hash2), "http://www.google.com")



