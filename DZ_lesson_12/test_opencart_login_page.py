from DZ_lesson_12.page_objects.UserLoginPage import UserLoginPage
from DZ_lesson_12.page_objects.Alert import Alert


# Тестируем страницу логина /index.php?route=account/login
def test_login_user_page_object(browser, url):
    # переходим на страницу логина user
    user_login_page = UserLoginPage(browser)
    user_login_page.open_page(url)
    user_login_page.log_in_as_user()
    user_email = user_login_page.USER_EMAIL
    browser.find_element_by_link_text('Edit Account').click()
    # получаем данные e-mail из Your Personal Details
    login_user_email = browser.execute_script('return document.getElementById("input-email").value;')
    assert login_user_email == user_email


def test_register_user_in_base(browser, url):
    # переходим на страницу логина user
    user_login_page = UserLoginPage(browser)
    user_login_page.open_page(url)
    user_login_page.register_user()
    alert_danger = Alert(browser).wait_danger_alert()
    assert alert_danger == 'Warning: E-Mail Address is already registered!'
