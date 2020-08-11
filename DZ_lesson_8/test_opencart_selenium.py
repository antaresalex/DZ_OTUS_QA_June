import pytest
import time
from selenium.webdriver.common.keys import Keys


# Тестируем сайт, что он связан с OpenCart
def test_example(browser, url):
    browser.get(url)
    browser.find_element_by_css_selector('footer p a').send_keys(Keys.END)
    element = browser.find_element_by_css_selector('a[href="http://www.opencart.com"]')
    assert element.text == 'OpenCart'


# Тестируем Главную /
# Тест 1 перемотки картинок на Главной (элемент становится видимым)
# <div class="swiper-pager">
#     <div class="swiper-button-next"></div>
#     <div class="swiper-button-prev"></div>
#   </div>
# Тест 2 последнего слайд-бара (перемотки) лого брендов
# Тест 3 открытия Privacy Policy
# <a href="http://localhost/index.php?route=information/information&amp;information_id=3">Privacy Policy</a>
# Тест 4-5 Featured Macbook открытия карточки с товаром по клику на картинку и по клику на название


# Каталог /index.php?route=product/category&path=20
# Карточку товара /index.php?route=product/product&path=57&product_id=49
# Страницу логина /index.php?route=account/login
# Страницу логина в админку /admin/