from django.test import TestCase
from selenium import webdriver

class TestCaseTradeToolPage(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_menu_link(self):

        self.browser.get('http://localhost:8000')

        # Log in
        self.browser.find_element_by_name('username').send_keys('test')
        password = self.browser.find_element_by_name('password')
        password.send_keys('test')
        password.submit()
        
        # Find 'Trade Tool' menu link
        navlist = self.browser.find_element_by_id('nav-list')
        links = navlist.find_elements_by_tag_name('li')
        trade_tool_link = (link for link in links if link.text == 'Trade Tool').next()
        self.assertIsNotNone(trade_tool_link)

