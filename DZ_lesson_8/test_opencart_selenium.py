import pytest
import time
from selenium.webdriver.common.keys import Keys


def test_example(browser, url):
    browser.get(url)
    browser.find_element_by_css_selector('footer p a').send_keys(Keys.END)
    element = browser.find_element_by_css_selector('a[href="http://www.opencart.com"]')
    assert element.text == 'OpenCart'
