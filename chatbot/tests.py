from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_url_returns_html_or_not(self):
        request = HttpRequest()
        response = home(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Jarvis</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
