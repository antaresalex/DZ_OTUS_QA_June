import BasePage


# открываем главную
# перематываем страницу вниз до конца (реализовано в _go_to_ бейз)
# перематываем страницу до элемента (реализовано в _go_to_element бейз)
# получаем название товара на Main Page из Featured
# получаем стоимость Featured продукта на Main Page
# кликаем на картинку Featured продукта
# клик на название Featured продукта
# перематываем первый слайд бар вперед
# делаем скриншот (сложно с названиями разыми постоянно, делаем в коде)
# сравниваем скриншоты (сложно с названиями разыми постоянно, делаем в коде)

class MainPage(BasePage):
    MAIN_PRODUCT_NAME = {'css': '.product-layout .caption a'}
    MAIN_PRODUCT_PICTURE = {'css': '.product-layout .img-responsive'}
    MAIN_PRODUCT_PRICE = {'css': '.product-layout .price'}
    MAIN_SLIDER_BUTTON_NEXT = {'css': '#content .swiper-button-next'}
    MAIN_PRIVACY_POLICY = {'css': 'body footer div div div:nth-child(1) ul li:nth-child(3) a'}

    def open_main_page(self, url):
        self.browser.get(url)

    def get_main_product_name(self, index=0):
        self._get_element_text(self.MAIN_PRODUCT_NAME, index)
        return self

    def get_main_product_price(self, index=0):
        price_element = self._get_element_text(self.MAIN_PRODUCT_PRICE, index)
        price_element = price_element.split('\n')[0]
        price_element = price_element.split(' ')[0]
        return price_element

    def click_main_product_name(self, index=0):
        self._click(self.MAIN_PRODUCT_NAME, index)
        return self

    def click_main_product_picture(self, index=0):
        self._click(self.MAIN_PRODUCT_PICTURE, index)
        return self

    def click_slider_button_next(self):
        self._click(self.MAIN_SLIDER_BUTTON_NEXT)
        return self

    def go_down(self):
        self._go_to_down_page()
        return self

    def get_text(self, selector):
        self._get_element_text(self, selector)
        return self

    def click_to_policy(self):
        self._click(self.MAIN_PRIVACY_POLICY)
        return self
