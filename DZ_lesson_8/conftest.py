import requests
import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from webdrivermanager import GeckoDriverManager
from selenium.webdriver import ChromeOptions
from webdrivermanager import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', '-B', action="store", default='chrome', required=False,
                     choices=['chrome', 'firefox'], help='choose browser for testing')
    parser.addoption("--url", "-U", action="store", default="http://localhost/", help="enter your url")


@pytest.fixture
def browser(request):
    browser_type = request.config.getoption('--browser')
    if browser_type == 'chrome':
        cdm = ChromeDriverManager()
        cdm.download_and_install()
        option = ChromeOptions()
        option.add_argument('--kiosk')
        # option.headless = True
        browser = webdriver.Chrome(options=option)
        browser.implicitly_wait(5)
        request.addfinalizer(browser.quit)
        return browser
    elif browser_type == 'firefox':
        gdm = GeckoDriverManager()
        gdm.download_and_install()
        option = FirefoxOptions()
        option.add_argument('--kiosk')
        # option.headless = True
        browser = webdriver.Firefox(options=option)
        browser.implicitly_wait(5)
        request.addfinalizer(browser.quit)
        return browser
    else:
        raise Exception(f'{request.param} is not supported!')


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
