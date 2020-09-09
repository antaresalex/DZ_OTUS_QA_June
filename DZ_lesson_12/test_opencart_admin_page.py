from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


# Тест перехода к разделу с товарами в админке, что появляется таблица с товарами.
def test_admin_product_table(browser, url, wait):
    # переходим в админку
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    # логинемся в админку
    browser.find_element_by_css_selector('#input-username').send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    # переходим в раздел Продукты каталога слева в админке
    browser.find_element_by_css_selector('#menu-catalog .collapsed').click()
    el = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#collapse1.collapse li:nth-child(2) a')))
    el.click()
    # проверяем наличие таблицы с продуктами в разделе
    table_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.table')))
    table_element_visible = table_element.is_displayed()
    assert table_element_visible is True


# Реализовать 2 тестовых сценария на раздел администратора
# Тест добавления нового продукта в каталог администратором
def test_admin_add_new_product(browser, url, wait):
    # переходим в админку
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    test_product = 'Test Product Name'
    # логинемся в админку
    browser.find_element_by_css_selector('#input-username').send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    # переходим в раздел Продукты каталога слева в админке
    browser.find_element_by_css_selector('#menu-catalog .collapsed').click()
    el = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#collapse1.collapse li:nth-child(2) a')))
    el.click()
    # добавляем новый продукт
    browser.find_element_by_css_selector('[data-original-title="Add New"]').click()
    browser.find_element_by_css_selector('#input-name1').send_keys(test_product)
    browser.find_element_by_css_selector('#input-meta-title1').send_keys(test_product)
    browser.find_element_by_link_text('Data').click()
    browser.find_element_by_css_selector('#input-model').send_keys('Product 15')
    browser.find_element_by_css_selector('[data-original-title="Save"]').click()
    browser.find_element_by_css_selector('#input-name').send_keys(test_product)
    browser.find_element_by_css_selector('.form-group #button-filter').click()
    product_table_content = browser.find_element_by_css_selector('tbody .text-left').text
    assert test_product == product_table_content


# Реализовать 2 тестовых сценария на раздел администратора
# Тест создания нового клиента через дашборд
def test_admin_add_new_customer(browser, url, wait):
    # переходим в админку
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    # логинемся в админку
    browser.find_element_by_css_selector('#input-username').send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    # переходим в раздел дашборда клиентов в админке
    browser.find_element_by_css_selector('.col-lg-3:nth-child(3) .tile-footer a').click()
    # добавляем нового клиента
    browser.find_element_by_css_selector('[data-original-title="Add New"]').click()
    browser.find_element_by_css_selector('#input-firstname').send_keys('Test')
    browser.find_element_by_css_selector('#input-lastname').send_keys('Test')
    browser.find_element_by_css_selector('#input-email').send_keys('test2@mail.ru')
    browser.find_element_by_css_selector('#input-telephone').send_keys('+79222222222')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    browser.find_element_by_css_selector('#input-password').send_keys('123456')
    browser.find_element_by_css_selector('#input-confirm').send_keys('123456')
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    browser.find_element_by_css_selector('[data-original-title="Save"]').click()
    # ждем успешного аллерта и получаем текст аллерта
    alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success')))
    # выделяем из текста аллерта текст до ":"
    text_alert = str(alert.text)
    success_text_alert = text_alert.split(':')[0]
    # удаляем второго добавленного клиента (user) из базы клиентов
    checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tbody tr:nth-child(2) input')))
    checkbox.click()
    browser.find_element_by_css_selector('[data-original-title="Delete"]').click()
    # так работает для чистки пользователя в firefox
    wait.until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    # так работает для чистки пользователя в chrome
    js_confirm = 'alert = function(){return true;}'
    browser.execute_script(js_confirm)
    browser.execute_script('return alert')
    assert success_text_alert == 'Success'
