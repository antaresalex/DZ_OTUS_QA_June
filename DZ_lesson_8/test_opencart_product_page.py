import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
# Тестируем карточку товара /index.php?route=product/product&path=57&product_id=49


# Тест добавляя в Wish list
@pytest.mark.parametrize("product_id", [40, 30, 36, 49])
def test_add_wish_list(browser, url, product_id):
    product_page_url = url + f'/index.php?route=product/product&path=57&product_id=' + str(product_id)
    browser.get(product_page_url)
    product_name = browser.find_element_by_css_selector('#content .col-sm-4 h1').text
    wish_list_button = browser.find_element_by_css_selector('[data-original-title="Add to Wish List"]')
    wish_list_button.click()
    alert = browser.find_element_by_css_selector('.alert-success')
    alert.find_element_by_link_text('login').click()
    browser.find_element_by_css_selector('#input-email').send_keys('test404@mail.ru')
    browser.find_element_by_css_selector('#input-password').send_keys('test')
    browser.find_element_by_css_selector('input[value=Login]').click()
    browser.find_element_by_link_text('Wish List').click()
    wish_list_product_name = browser.find_element_by_link_text(product_name).text
    assert wish_list_product_name == product_name


# Тест добавления в Cart
@pytest.mark.parametrize("product_id", [36, 49])
def test_add_cart(browser, url, product_id):
    product_page_url = url + f'/index.php?route=product/product&path=57&product_id=' + str(product_id)
    browser.get(product_page_url)
    product_name = browser.find_element_by_css_selector('#content .col-sm-4 h1').text
    # try:
    #     select = Select(browser.find_element_by_tag_name('select'))
    #     select.select_by_index(1)
    # except NoSuchElementException:
    #     raise NoSuchElementException('Select is not found')
    # finally:
    cart_button = browser.find_element_by_css_selector('#button-cart')
    cart_button.click()
    time.sleep(3)
    alert = browser.find_element_by_css_selector('.alert-success')
    alert.find_element_by_link_text('shopping cart').click()
    time.sleep(3)
    cart_product_name = browser.find_element_by_link_text(product_name).text
    assert cart_product_name == product_name


# Тест Like #u_0_1 > button > span
# Тест написания ревью #input-name
# Тест совпадения названия с название сверху #product-product > ul > li:nth-child(3) > a
