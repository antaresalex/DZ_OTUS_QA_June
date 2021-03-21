import BasePage


# переходим на страницу логина user
# логинемся как user
# переходим в виш лист со страницы аккаунта user
# переходим в Edit Account со страница аккаунта user
# вводим данные user-а

class UserLoginPage(BasePage):
    USER_LOGIN_URL = f'/index.php?route=account/login'
    USER_EMAIL = 'test404@mail.ru'
    USER_PASSWORD = 'test'
    USER_TEL = '+79111111111'
    USER_FIRST_NAME = 'Test'
    USER_LAST_NAME = 'Test'
    LOGIN_FORM = {'css': '.well form'}
    REGISTER_FORM = {'css': '.well a'}
    REGISTER_CONTINUE = 'Continue'
    INPUT_EMAIL = {'css': '#input-email'}
    INPUT_PASSWORD = {'css': '#input-password'}
    INPUT_TEL = {'css': '#input-telephone'}
    INPUT_FIRST_NAME = {'css': '#input-firstname'}
    INPUT_LAST_NAME = {'css': '#input-lastname'}
    INPUT_CONFIRM_PASSWORD = {'css': '#input-confirm'}
    LOGIN_BUTTON = {'css': 'input[value=Login]'}
    NEWSLETTER_CHECKBOX = {'css': '[type="checkbox"]'}
    SUBMIT_BUTTON = {'css': '[type="submit"]'}
    EDIT_ACCOUNT_BUTTON = 'Edit Account'
    WISH_LIST = 'Wish List'

    def open_page(self, url):
        user_login_url = url + self.USER_LOGIN_URL
        self.browser.get(user_login_url)

    def log_in_as_user(self):
        self._wait_for_visible(self.LOGIN_FORM)
        self._input(self.INPUT_EMAIL, self.USER_EMAIL)
        self._input(self.INPUT_PASSWORD, self.USER_PASSWORD)
        self._click(self.LOGIN_BUTTON)
        return self

# не работает с передачей линка а не селектора
    def edit_account(self):
        self._click(selector=None, index=0, link_text=self.EDIT_ACCOUNT_BUTTON)
        return self

    def go_to_wish_list_from_account(self):
        self._click(selector=None, index=0, link_text=self.WISH_LIST)
        return self

    def register_user(self):
        self._wait_for_visible(self.REGISTER_FORM)
        # self._click(self.REGISTER_CONTINUE)
        self.browser.find_element_by_link_text('Continue').click()
        self._input(self.INPUT_EMAIL, self.USER_EMAIL)
        self._input(self.INPUT_TEL, self.USER_TEL)
        self._input(self.INPUT_FIRST_NAME, self.USER_FIRST_NAME)
        self._input(self.INPUT_LAST_NAME, self.USER_LAST_NAME)
        self._input(self.INPUT_PASSWORD, self.USER_PASSWORD)
        self._input(self.INPUT_CONFIRM_PASSWORD, self.USER_PASSWORD)
        self._click(self.NEWSLETTER_CHECKBOX)
        self._click(self.SUBMIT_BUTTON)
        return self
