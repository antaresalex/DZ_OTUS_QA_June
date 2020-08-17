# Тест страницы логина в админку /admin/

# Тестируем логин уже существующего пользователя
def test_login_user(browser, url):
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    user_email = 'user@example.com'
    browser.find_element_by_css_selector('#input-username').send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    browser.find_element_by_css_selector('.fa-caret-down').click()
    browser.find_element_by_css_selector('.nav .dropdown-menu-right a').click()
    login_user_email = browser.execute_script('return document.getElementById("input-email").value;')
    assert login_user_email == user_email


# Тестируем логин несуществующего пользователя
def test_login_incorrect_user(browser, url):
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'gggg'
    user_password = '5533'
    browser.find_element_by_css_selector('#input-username').send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    alert_danger = browser.find_element_by_css_selector('.alert-dismissible')
    displayed_alert = alert_danger.is_displayed()
    assert displayed_alert is True
