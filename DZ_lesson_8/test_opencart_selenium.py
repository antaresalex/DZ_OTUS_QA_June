import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Тестируем сайт, что он связан с OpenCart
def test_example(browser, url):
    browser.get(url)
    browser.find_element_by_css_selector('footer p a').send_keys(Keys.END)
    time.sleep(5)
    element = browser.find_element_by_css_selector('a[href="http://www.opencart.com"]')
    assert element.text == 'OpenCart'


# Тестируем Главную /
# Тест 1 открытия Privacy Policy
def test_click_privacy_policy(browser, url):
    browser.get(url)
    browser.find_element_by_css_selector('body footer div div div:nth-child(1) ul li:nth-child(3) a').send_keys(
        Keys.END)
    element = browser.find_element_by_css_selector('body footer div div div:nth-child(1) ul li:nth-child(3) a')
    element.click()
    new_pade_element = browser.find_element_by_css_selector('#content h1')
    assert new_pade_element.text == 'Privacy Policy'


# Тестируем Главную /
# Тест 2 Featured Macbook открытия карточки с товаром по клику на картинку
def test_click_featured_picture(browser, url):
    browser.get(url)
    element = browser.find_element_by_css_selector('.product-layout .img-responsive')
    actions = ActionChains(browser)
    actions.move_to_element(element)
    name_element = browser.find_element_by_css_selector('.product-layout .caption a').text
    actions.perform()
    element.click()
    new_pade_element = browser.find_element_by_css_selector('#content .col-sm-4 h1')
    assert new_pade_element.text == name_element


# Тестируем Главную /
# Тест 3 Featured Macbook открытия карточки с товаром по клику на название
def test_click_featured_name(browser, url):
    browser.get(url)
    element = browser.find_element_by_css_selector('.product-layout .caption a')
    actions = ActionChains(browser)
    actions.move_to_element(element)
    name_element = browser.find_element_by_css_selector('.product-layout .caption a').text
    actions.perform()
    element.click()
    new_pade_element = browser.find_element_by_css_selector('#content .col-sm-4 h1')
    assert new_pade_element.text == name_element


# Тестируем Главную /
# Тест 4 Featured по стоимости
def test_featured_price(browser, url):
    browser.get(url)
    price_element = browser.find_element_by_css_selector('.product-layout .price')
    price_element.location_once_scrolled_into_view
    price_element = str(browser.find_element_by_css_selector('.product-layout .price').text)
    price_element = price_element.split('\n')[0]
    element = browser.find_element_by_css_selector('.product-layout .caption a')
    element.click()
    new_pade_element = browser.find_element_by_css_selector('#content .row .col-sm-4 h2')
    print(new_pade_element.text)
    assert new_pade_element.text == price_element


# Тестируем Главную /
# Тест 5 Переключение картинок в первом слайдбаре
def test_show_next_slide(browser, url):
    browser.get(url)
    try:
        element_size = browser.find_element_by_css_selector(
            "#slideshow0 > div > div.swiper-slide.text-center.swiper-slide-active > img").size
    except NoSuchElementException:
        time.sleep(3)
        swiper = browser.find_element_by_css_selector('#content .swiper-button-next')
        swiper.click()
        element_size = browser.find_element_by_css_selector(
            "#slideshow0 > div > div.swiper-slide.text-center.swiper-slide-active > img").size
    assert element_size != 0


# Каталог /index.php?route=product/category&path=20
# Карточку товара /index.php?route=product/product&path=57&product_id=49
# Страницу логина /index.php?route=account/login
# Страницу логина в админку /admin/
