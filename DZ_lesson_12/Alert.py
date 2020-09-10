# ждем успешного аллерта
# переходим из аллерта в логин
# переходим из аллерта в виш лист
# переходим из аллерта в корзину
# ждем danger аллерта

from .BasePage import BasePage


class Alert(BasePage):
    SUCCESS_ALERT = {'css': '.alert-success'}
    SUCCESS_ALERT_LOGIN = {'text': 'login'}
    SUCCESS_ALERT_TO_CART = {'css': SUCCESS_ALERT['css'] + ' > a:nth-child(2)'}
    SUCCESS_ALERT_TO_WISH_LIST = {'text': 'wish list'}
    DANGER_ALERT = {'css': '.alert-danger'}

    def wait_success_alert(self):
        self._wait_for_visible(self.SUCCESS_ALERT['css'])
        return self

    def click_login(self):
        self.browser.find_element_by_link_text(self.SUCCESS_ALERT_LOGIN['text']).click()

    def click_to_cart(self):
        self.browser.find_element_by_css_selector(self.SUCCESS_ALERT_TO_CART['css']).click()

    def click_to_wish_list(self):
        self.browser.find_element_by_link_text(self.SUCCESS_ALERT_TO_WISH_LIST['text']).click()

    def wait_danger_alert(self):
        self._wait_for_visible(self.DANGER_ALERT['css'])
        return self
