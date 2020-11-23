# открываем каталог
# перематываем страницу до элемента (исп из бейз)
# получаем название раздела из залоговка каталога
# переходим в раздел каталога из меню-списка слева (оставляем в коде)
# добавляем товар в сравнение
# переходим в список сравнения выбранных товаров

from .BasePage import BasePage


class CatalogPage(BasePage):
    CATALOG_URL = f'/index.php?route=product/category&path='
    SECTION_NAME = {'css': '#content h2'}
    CATALOG_LIST = {'css': '.list-group'}
    COMPARE_BUTTON = {'css': '[data-original-title="Compare this Product"]'}
    ALL_COMPARE_LIST = {'css': '#compare-total'}

    def open_page(self, url, product_id=20):
        catalog_page_url = url + self.CATALOG_URL + str(product_id)
        self.browser.get(catalog_page_url)

    def get_catalog_section_name(self):
        self._get_element_text(self.SECTION_NAME)
        return self

    def add_to_compare(self):
        self._click(self.COMPARE_BUTTON)
        return self

    def go_to_compare_list(self):
        self._wait_for_visible(self.ALL_COMPARE_LIST)
        self._click(self.ALL_COMPARE_LIST)
        return self
