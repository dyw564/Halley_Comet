"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from django.test.client import Client

from bit.models import Url
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class Test_Index(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        Url.objects.create(long_url="www.baidu.com", short_url="aaaaab")
        Url.objects.create(long_url="www.sina.com", short_url="aaaaac")


    def test_details(self):
        response = self.client.get('/index/')

        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['user_data']),2)
