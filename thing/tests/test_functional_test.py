from django.test import TestCase
from itertools import chain
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
        # The page has an expected title
        self.assertEqual(self.browser.title, 'EVEthing: Trade Tool')
        # The page has a similar style to the other pages
        self.assertIsNotNone(self.browser.find_element_by_name('viewport'))
        self.assertIsNotNone(self.browser.find_element_by_class_name('navbar-header'))
        # The page does not have any trade plan elements yet
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_tag_name('h2')
        
        # She enters here current location
        system_input = self.browser.find_element_by_name('system')
        system_input.send_keys('test')
        system_input.submit()
        
        # The tool tells her what to buy, where to buy it and where to sell it
        result_header = self.browser.find_element_by_tag_name('h2')
        self.assertEqual(result_header.text, 'Best Trade')

        table_headers = self.browser.find_elements_by_tag_name('th')
        table_cells = self.browser.find_elements_by_tag_name('td')
        mock_table_data = (
            'Item',
            'Pickup',
            'Drop Off',
            'Buy Up To',
            'Amount',
            'Sell Down To',
            'Tritanium',
            'Jita 4-4 Caldari Business Tribunal Information Center',
            'Amarr 6-2 Theology Council Tribunal',
            6.36,
            44000,
            7.63
        )

        for cell in chain(table_headers, table_cells):
            self.assertIn(cell.text, mock_table_data)

        self.fail('finish test')
