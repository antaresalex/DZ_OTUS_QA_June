from .BasePage import BasePage

# открываем страницу продукта
# product_page_url = url + f'/index.php?route=product/product&path=57&product_id='

# получаем название товара на странице из заголовка
# нажимаем на добавить в виш лист add_to_wish_list
# нажимаем на добавить в корзину add_to_cart
# открываем написание ревью open_review
# отправляем ревью send_review
# получаем имя продукта на странице
# получаем стоимость продукта на Product Page


class ProductPage(BasePage):

    PRODUCT_PAGE_URL = f'/index.php?route=product/product&path=57&product_id='
    ADD_TO_WISHLIST = {'css': '[data-original-title="Add to Wish List"]'}
    ADD_TO_CART = {'css': '#button-cart'}
    PRODUCT_NAME = {'css': '#content .col-sm-4 h1'}
    CLICK_REVIEW = {'css': '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active > a'}
    SEND_REVIEW = {'css': '.pull-right #button-review'}

    def open_page(self, url, product_id):
        product_page_url = url + self.PRODUCT_PAGE_URL + str(product_id)
        self.browser.get(product_page_url)

    def add_to_wishlist(self):
        self._click(self.ADD_TO_WISHLIST)
        return self

    def add_to_cart(self):
        self._click(self.ADD_TO_CART)
        return self

    def get_product_name(self):
        product_name_text = self._get_element_text(self.PRODUCT_NAME)
        return product_name_text

    def get_cart_name_from_page(self):
        cart_product_name = self._get_element_text(self.get_product_name())
        return cart_product_name

    def click_review(self):
        self._click(self.CLICK_REVIEW)
        return self

    def send_review(self):
        self._click(self.SEND_REVIEW)
        return self
