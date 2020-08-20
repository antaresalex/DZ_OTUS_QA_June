import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Добавить явные ожидания


# Тест перехода к разделу с товарами в админке, что появляется таблица с товарами.
def test_admin_product_table(browser, url, wait):
    admin_login_page_url = url + f'/admin/'
    browser.get(admin_login_page_url)
    user_name = 'user'
    user_password = 'bitnami1'
    browser.find_element_by_css_selector('#input-username').send_keys(user_name)
    browser.find_element_by_css_selector('#input-password').send_keys(user_password)
    browser.find_element_by_css_selector('[type="submit"]').click()
    browser.find_element_by_css_selector('.fa-caret-down').click()
    browser.find_element_by_css_selector('#menu-catalog .collapsed').click()
    el = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#collapse1.collapse li:nth-child(2) a')))
    el.click()
    table_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.table')))
    table_element_visible = table_element.is_displayed()
    assert table_element_visible is True


# Реализовать 2 тестовых сценария на раздел администратора
# Тест добавления нового продукта в каталог администратором
# def test_admin_add_new_product(browser, url):
    # browser.get(url)
    # element = browser.find_element_by_css_selector('.product-layout .img-responsive')
    # actions = ActionChains(browser)
    # actions.move_to_element(element)
    # name_element = browser.find_element_by_css_selector('.product-layout .caption a').text
    # actions.perform()
    # element.click()
    # new_pade_element = browser.find_element_by_css_selector('#content .col-sm-4 h1')
    # assert new_pade_element.text == name_element


# Тест создания нового счета для отображения в дашборде
