from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Тест страницы логина в админку /admin/

# Тестируем логин уже существующего пользователя
def test_login_admin(browser, url, wait):
    # переходим в админку
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    user_email = 'user@example.com'
    # логинемся в админку
    login_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    login_page.send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    # переходим в профиль рядом с аватаркой админа
    el = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-caret-down')))
    el.click()
    browser.find_element_by_css_selector('.nav .dropdown-menu-right a').click()
    # получаем эмейл в профиле
    login_user_email = browser.execute_script('return document.getElementById("input-email").value;')
    assert login_user_email == user_email


# Тестируем логин несуществующего пользователя
def test_login_incorrect_admin(browser, url, wait):
    # переходим в админку
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'gggg'
    user_password = '5533'
    # логинемся в админку
    login_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    login_page.send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    # ждем danger аллерта
    alert_danger = browser.find_element_by_css_selector('.alert-danger')
    displayed_alert = alert_danger.is_displayed()
    assert displayed_alert is True


# Тестирование разлогина раздела администратора
def test_logout_admin(browser, url, wait):
    # переходим в админку
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    # логинемся в админку
    login_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    login_page.send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    # разлогинеться
    el = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-caret-down')))
    el.click()
    browser.find_element_by_css_selector('.navbar-nav li:nth-child(2) a').click()
    # получаем текст заголовка страницы логина админа
    enter_login_info = browser.find_element_by_css_selector('.panel-title').text
    assert enter_login_info == 'Please enter your login details.'
