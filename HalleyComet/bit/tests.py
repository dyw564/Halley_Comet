"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bit.models import Url

from django.utils import unittest
import unittest
    	
class Test(TestCase):
    def setUp(self):
       long_url = "www.baidu.com"
       long_url1 = "http://www.baidu.com"
       self.asserEqual(1 + 1, 3)
       self.asserEqual(judgment(long_url), "www.baidu.com")
       self.asserEqual(judgment(long_url1), "http://www.baidu.com")
    







