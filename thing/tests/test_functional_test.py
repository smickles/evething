from django.test import TestCase
from selenium import webdriver
from thing.tests.common_things import login

class TestCaseTradeTool(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_basic_usage(self):
        # Alice logs in
        login(self.browser)
        
        # She navigates to the trade tool
        self.browser.get('http://localhost:8000/trade_tool/')
        
        # She enters here current location
        system_input = self.browser.find_element_by_name('system')
        system_input.send_keys('Jita')
        system_input.submit()
        
        # The tool tells her what to buy, where to buy it and where to sell it
        self.fail('finish test')
