import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.views import SignUpView


class AccountsTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)
        
    def test_home_page_status_code(self):
        response = self.client.get('/signup.html')