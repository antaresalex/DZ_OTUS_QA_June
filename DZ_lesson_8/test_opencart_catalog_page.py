import pytest


# Тест каталога /index.php?route=product/category&path=20

# Тест добавления в сравнение Compare
@pytest.mark.parametrize("product_index", [1, 5, 11])
def test_add_to_compare(browser, url, product_index):
    catalog_page_url = url + f'/index.php?route=product/category&path=20'
    browser.get(catalog_page_url)
    first_product = browser.find_elements_by_css_selector('.product-grid')[0]
    first_product.location_once_scrolled_into_view
    compare_button = first_product.find_element_by_css_selector('[data-original-title="Compare this Product"]')
    compare_button.click()
    second_product = browser.find_elements_by_css_selector('.product-grid')[product_index]
    second_product.location_once_scrolled_into_view
    second_product_name_js = str(
        f'return document.querySelectorAll(".product-layout .img-responsive")[' + str(product_index) + f'].title;')
    second_product_name = browser.execute_script(second_product_name_js)
    second_compare_button = second_product.find_element_by_css_selector('[data-original-title="Compare this Product"]')
    second_compare_button.click()
    compare_link = browser.find_element_by_css_selector('#compare-total')
    compare_link.click()
    second_compare_product = browser.find_elements_by_css_selector('#content tbody tr strong')[1].text
    assert second_compare_product == second_product_name


# Тест клика по #column-left > div.list-group на Desktops что мы точно на Desktops по тексту #content > h2
@pytest.mark.parametrize("catalog_id", [20, 34, 18])
def test_catalog_name(browser, url, catalog_id):
    catalog_page_url = url + f'/index.php?route=product/category&path=' + str(catalog_id)
    browser.get(catalog_page_url)
    catalog_name = browser.find_element_by_css_selector('#content h2').text
    other_catalog_list = browser.find_element_by_css_selector('.list-group')
    other_catalog_list.find_element_by_partial_link_text(catalog_name).click()
    new_catalog_name = browser.find_element_by_css_selector('#content h2').text
    assert new_catalog_name == catalog_name
