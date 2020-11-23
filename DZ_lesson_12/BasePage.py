from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.browser.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        ActionChains(self.browser).move_to_element(self.__element(selector, index)).click().perform()

    def _go_to_element(self, selector, link_text=None, index=0):
        return self.__element(selector, index, link_text).location_once_scrolled_into_view

    def _go_to_down_page(self):
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def _go_up_page(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=3):
        return WebDriverWait(self.browser, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    # получаем текст или получаем продукт по имени на любой странице по поиску по тексту
    def _get_element_text(self, selector, link_text=None, index=0):
        return self.__element(selector, index, link_text).text
