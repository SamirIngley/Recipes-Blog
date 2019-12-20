from django.urls import reverse
from django.test import TestCase

from .models import Page

def create_page(name, text):
    """
    Create a  with the given `author` and 'content' Negative or Positive.
    """
    return Page.objects.create(author = author, context = text)

class IndexViewTests(TestCase):
    def test_no_pages(self):
        """
        If no s exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_page_list'], [])

    def test_past_page(self):
        """
        pages with a pub_date in the past are displayed on the
        index .
        """
        create_page(page_text="Past page.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_page_list'],
            ['<page: Past page.>']
        )

    def test_future_page(self):
        """
        pages with a pub_date in the future aren't displayed on
        the index .
        """
        create_page(page_text="Future page.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_page_list'], [])

    def test_future_page_and_past_page(self):
        """
        Even if both past and future pages exist, only past pages
        are displayed.
        """
        create_page(page_text="Past page.", days=-30)
        create_page(page_text="Future page.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_page_list'],
            ['<page: Past page.>']
        )

    def test_two_past_pages(self):
        """
        The pages index  may display multiple pages.
        """
        create_page(page_text="Past page 1.", days=-30)
        create_page(page_text="Past page 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_page_list'],
            ['<page: Past page 2.>', '<page: Past page 1.>']
        )