from selenium import webdriver
import unittest


class BrowserTitleTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'/opt/geckodriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_to_check_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Jarvis', self.browser.title)
        self.fail('finish the test')


if __name__ == '__main__':
    unittest.main()
