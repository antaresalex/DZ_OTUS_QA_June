from DZ_lesson_12.page_objects.BasePage import BasePage


# переходим в админку
# логинемся в админку
# логинемся в админку некорректно
# переходим в профиль рядом с аватаркой админа
# разлогинеться
# получаем текст заголовка страницы логина админа
# переходим в раздел Продукты каталога слева в админке
# добавляем новый продукт
# добавляем нового клиента
# удаляем второго добавленного клиента (user) из базы клиентов

class AdminPage(BasePage):
    ADMIN_PAGE = f'/admin/'
    ADMIN_NAME = 'user'
    ADMIN_PASSWORD = 'bitnami1'
    ADMIN_EMAIL = 'user@example.com'
    INCORRECT_ADMIN_NAME = 'gggg'
    INCORRECT_ADMIN_PASSWORD = '5533'
    SUBMIT_BUTTON = {'css': '[type="submit"]'}
    INPUT_ADMIN_NAME = {'css': '#input-username'}
    INPUT_ADMIN_PASSWORD = {'css': '#input-password'}
    ADMIN_LOGOUT = {'css': '.navbar-nav li:nth-child(2) a'}
    ADMIN_DROP_DOWN = {'css': '.fa-caret-down'}
    ADMIN_PROFILE = {'css': '.nav .dropdown-menu-right a'}
    ADMIN_PANEL_TITLE = {'css': '.panel-title'}
    ADMIN_ALL_CATALOG = {'css': '#menu-catalog .collapsed'}
    ADMIN_PRODUCT_CATALOG = {'css': '#collapse1.collapse li:nth-child(2) a'}
    TEST_PRODUCT = 'Test Product Name'
    NEW_PRODUCT_BUTTON = {'css': '[data-original-title="Add New"]'}
    INPUT_PRODUCT_NAME = {'css': '#input-name1'}
    INPUT_PRODUCT_NAME_FINAL = {'css': '#input-name'}
    INPUT_TAG = {'css': '#input-meta-title1'}
    INPUT_MODEL = {'css': '#input-model'}
    FILTER_FORM_BUTTON = {'css': '.form-group #button-filter'}
    SAVE_PRODUCT_INFO = {'css': '[data-original-title="Save"]'}
    PRODUCT_TEXT = {'css': 'tbody .text-left'}
    NEW_PRODUCT_DATA = 'Data'
    NEW_PRODUCT_MODEL = 'Product 15'
    CLIENT = {'css': 'tbody tr:nth-child(2) input'}
    DELETE_BUTTON = {'css': '[data-original-title="Delete"]'}
    NEW_CLIENT_BUTTON = {'css': '[data-original-title="Add New"]'}
    INPUT_FIRST_NAME_CLIENT = {'css': '#input-firstname'}
    INPUT_LAST_NAME_CLIENT = {'css': '#input-lastname'}
    INPUT_EMAIL_CLIENT = {'css': '#input-email'}
    INPUT_TEL_CLIENT = {'css': '#input-telephone'}
    INPUT_PASSWORD_CLIENT = {'css': '#input-password'}
    CLIENT_NAME = 'Test'
    CLIENT_EMAIL = 'test2@mail.ru'
    CLIENT_TEL = '+79222222222'
    CLIENT_PASSWORD = '123456'
    INPUT_CLIENT_CONFIRM = {'css': '#input-confirm'}
    SAVE_CLIENT = {'css': '[data-original-title="Save"]'}

    def open_page(self, url):
        admin_url = url + self.ADMIN_PAGE
        self.browser.get(admin_url)

    def log_in_admin(self):
        self._wait_for_visible(self.INPUT_ADMIN_NAME)
        self._input(self.INPUT_ADMIN_NAME, self.ADMIN_NAME)
        self._input(self.INPUT_ADMIN_PASSWORD, self.ADMIN_PASSWORD)
        self._click(self.SUBMIT_BUTTON)
        return self

    def log_in_incorrect_admin(self):
        self._wait_for_visible(self.INPUT_ADMIN_NAME)
        self._input(self.INPUT_ADMIN_NAME, self.INCORRECT_ADMIN_NAME)
        self._input(self.INPUT_ADMIN_PASSWORD, self.INCORRECT_ADMIN_PASSWORD)
        self._click(self.SUBMIT_BUTTON)
        return self

    def logout(self):
        self._wait_for_visible(self.ADMIN_LOGOUT)
        self._click(self.ADMIN_LOGOUT)
        return self

    def go_to_profile(self):
        self._wait_for_visible(self.ADMIN_DROP_DOWN)
        self._click(self.ADMIN_DROP_DOWN)
        self._click(self.ADMIN_PROFILE)
        return self

    def get_admin_panel_text(self):
        self._get_element_text(self.ADMIN_PANEL_TITLE)
        return self

    def go_to_product_catalog(self):
        self._click(self.ADMIN_ALL_CATALOG)
        self._wait_for_visible(self.ADMIN_PRODUCT_CATALOG)
        self._click(self.ADMIN_PRODUCT_CATALOG)
        return self

    def add_new_product(self):
        self._click(self.NEW_PRODUCT_BUTTON)
        self._input(self.INPUT_PRODUCT_NAME, self.TEST_PRODUCT)
        self._input(self.INPUT_TAG, self.TEST_PRODUCT)
        self._click(self.NEW_PRODUCT_DATA)
        self._input(self.INPUT_MODEL, self.TEST_PRODUCT)
        self._click(self.SAVE_PRODUCT_INFO)
        self._input(self.INPUT_PRODUCT_NAME_FINAL, self.TEST_PRODUCT)
        self._click(self.FILTER_FORM_BUTTON)
        product_table_content = self._get_element_text(self.PRODUCT_TEXT)
        return product_table_content

    def add_new_client(self):
        self._click(self.NEW_CLIENT_BUTTON)
        self._input(self.INPUT_FIRST_NAME_CLIENT, self.CLIENT_NAME)
        self._input(self.INPUT_LAST_NAME_CLIENT, self.CLIENT_NAME)
        self._input(self.INPUT_EMAIL_CLIENT, self.CLIENT_EMAIL)
        self._input(self.INPUT_TEL_CLIENT, self.CLIENT_TEL)
        self._go_to_down_page()
        self._input(self.INPUT_PASSWORD_CLIENT, self.CLIENT_PASSWORD)
        self._input(self.INPUT_CLIENT_CONFIRM, self.CLIENT_PASSWORD)
        self._go_up_page()
        self._click(self.SAVE_CLIENT)

    def delete_client(self):
        self._wait_for_visible(self.CLIENT)
        self._click(self.CLIENT)
        self._click(self.DELETE_BUTTON)
