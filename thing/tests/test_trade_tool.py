from django.test import TestCase
from selenium import webdriver
from thing.tests.common_things import login

class TestCaseTradeToolPage(TestCase):

    def setUp(self):
        # Log in
        self.browser = webdriver.Firefox()
        login(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_menu_link(self):
        # Find 'Trade Tool' menu link
        navlist = self.browser.find_element_by_id('nav-list')
        links = navlist.find_elements_by_tag_name('li')
        trade_tool_link = (link for link in links if link.text == 'Trade Tool').next()
        self.assertIsNotNone(trade_tool_link)
