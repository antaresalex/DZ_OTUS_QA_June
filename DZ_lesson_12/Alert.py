# ждем успешного аллерта
# переходим из аллерта в логин
# переходим из аллерта в виш лист
# переходим из аллерта в корзину
# ждем danger аллерта

from .BasePage import BasePage


class Alert(BasePage):
    SUCCESS_ALERT = {'css': '.alert-success'}
    SUCCESS_ALERT_LOGIN = 'login'
    SUCCESS_ALERT_TO_CART = {'css': SUCCESS_ALERT['css'] + ' > a:nth-child(2)'}
    SUCCESS_ALERT_TO_WISH_LIST = 'wish list'
    DANGER_ALERT = {'css': '.alert-danger'}

    def wait_success_alert(self):
        self._wait_for_visible(self.SUCCESS_ALERT)
        return self

    def click_login(self):
        self._click(self.SUCCESS_ALERT_LOGIN)

    def click_to_cart(self):
        self._click(self.SUCCESS_ALERT_TO_CART)

    def click_to_wish_list(self):
        self._click(self.SUCCESS_ALERT_TO_WISH_LIST)

    def wait_danger_alert(self):
        self._wait_for_visible(self.DANGER_ALERT)
        return self
