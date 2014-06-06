def login(browser):
    browser.get('http://localhost:8000')
    browser.find_element_by_name('username').send_keys('test')
    password = browser.find_element_by_name('password')
    password.send_keys('test')
    password.submit()