import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Тестируем карточку товара /index.php?route=product/product&path=57&product_id=49


# Тест добавляя в Wish list
@pytest.mark.parametrize("product_id", [40, 30, 36, 49])
def test_add_wish_list(browser, url, product_id, wait):
    # открываем страницу продукта
    product_page_url = url + f'/index.php?route=product/product&path=57&product_id=' + str(product_id)
    browser.get(product_page_url)
    # получаем название товара на странице из заголовка
    product_name = browser.find_element_by_css_selector('#content .col-sm-4 h1').text
    # нажимаем на добавить в виш лист
    wish_list_button = browser.find_element_by_css_selector('[data-original-title="Add to Wish List"]')
    wish_list_button.click()
    # ждем успешного аллерта и получаем текст аллерта
    alert = wait.until((EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success'))))
    # переходим из аллерта в логин (надо переходить в виш лист, а логинется до теста)
    alert.find_element_by_link_text('login').click()
    # логинемся как user
    browser.find_element_by_css_selector('#input-email').send_keys('test404@mail.ru')
    browser.find_element_by_css_selector('#input-password').send_keys('test')
    browser.find_element_by_css_selector('input[value=Login]').click()
    # переходим в виш лист со страницы аккаунта user
    browser.find_element_by_link_text('Wish List').click()
    # получаем имя продукта на странице
    wish_list_product_name = browser.find_element_by_link_text(product_name).text
    assert wish_list_product_name == product_name


# Тест добавления в Cart
@pytest.mark.parametrize("product_id", [47, 40, 30, 36, 49])
def test_add_cart(browser, url, product_id, wait):
    # открываем страницу продукта
    product_page_url = url + f'/index.php?route=product/product&path=57&product_id=' + str(product_id)
    browser.get(product_page_url)
    # получаем название товара на странице из заголовка
    product_name = browser.find_element_by_css_selector('#content .col-sm-4 h1').text
    select = browser.find_elements_by_tag_name('select')
    if len(select) != 0:
        select = Select(select[0])
        select.select_by_index(1)
    # нажимаем на добавить в корзину
    cart_button = browser.find_element_by_css_selector('#button-cart')
    cart_button.click()
    # ждем успешного аллерта и получаем текст аллерта
    alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success')))
    # переходим из аллерта в корзину
    alert.find_element_by_link_text('shopping cart').click()
    # получаем имя продукта на странице
    cart_product_name = browser.find_element_by_link_text(product_name).text
    assert cart_product_name == product_name


# Тест написания ревью #input-name
@pytest.mark.parametrize("product_id", [47, 40, 30, 36, 49])
def test_reviews(browser, url, product_id, wait):
    # открываем страницу продукта
    product_page_url = url + f'/index.php?route=product/product&path=57&product_id=' + str(product_id)
    browser.get(product_page_url)
    time.sleep(3)
    # открываем написание ревью
    reviews = browser.find_element_by_css_selector('.nav-tabs').find_element_by_partial_link_text('Reviews')
    reviews.click()
    # заполняем поля ревью верными данными
    reviews_name = browser.find_element_by_css_selector('#input-name')
    reviews_name.send_keys('Test Test')
    reviews_text = browser.find_element_by_css_selector('#input-review')
    reviews_text.send_keys('It is really good product. Test Test Test Test Test Test Test Test Test Test Test')
    rating = browser.find_elements_by_css_selector("[name='rating']")
    rating[4].click()
    # отправляем ревью
    browser.find_element_by_css_selector('.pull-right #button-review').send_keys(Keys.END)
    button = browser.find_element_by_css_selector('.pull-right #button-review')
    button.click()
    # ждем успешного аллерта и получаем текст аллерта
    alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success')))
    alert_text = str(alert.text)
    # берем часть текста аллерта до точки
    alert_text_thank = alert_text.split('.')[0]
    assert alert_text_thank == 'Thank you for your review'
