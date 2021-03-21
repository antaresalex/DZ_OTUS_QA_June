import BasePage

# открываем страницу продукта
# product_page_url = url + f'/index.php?route=product/product&path=57&product_id='

# получаем название товара на странице из заголовка
# нажимаем на добавить в виш лист add_to_wish_list
# нажимаем на добавить в корзину add_to_cart
# открываем написание ревью open_review
# отправляем ревью send_review
# получаем продукт по имени на любой странице по поиску по тексту (уносим в бейз)
# получаем стоимость продукта на Product Page


class ProductPage(BasePage):

    PRODUCT_PAGE_URL = f'/index.php?route=product/product&path=57&product_id='
    ADD_TO_WISHLIST = {'css': '[data-original-title="Add to Wish List"]'}
    ADD_TO_CART = {'css': '#button-cart'}
    PRODUCT_NAME = {'css': '#content .col-sm-4 h1'}
    PRODUCT_PRICE = {'css': 'content .row .col-sm-4 h2'}
    CLICK_REVIEW = {'css': '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active > a'}
    SEND_REVIEW = {'css': '.pull-right #button-review'}

    def open_page(self, url, product_id=49):
        product_page_url = url + self.PRODUCT_PAGE_URL + str(product_id)
        self.browser.get(product_page_url)

    def add_to_wishlist(self):
        self._click(self.ADD_TO_WISHLIST)
        return self

    def add_to_cart(self):
        self._click(self.ADD_TO_CART)
        return self

    def get_product_name(self):
        self._get_element_text(self.PRODUCT_NAME)
        return self

    def get_cart_name_from_page(self):
        self._get_element_text(self.get_product_name())
        return self

    def click_review(self):
        self._wait_for_visible(self.CLICK_REVIEW)
        self._click(self.CLICK_REVIEW)
        return self

    def send_review(self):
        self._click(self.SEND_REVIEW)
        return self

    def get_product_price(self):
        self._get_element_text(self.PRODUCT_PRICE)
        return self
