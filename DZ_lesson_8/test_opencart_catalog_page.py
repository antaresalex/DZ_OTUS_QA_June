import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Тест каталога /index.php?route=product/category&path=20

# Тест добавления в сравнение Compare
@pytest.mark.parametrize("product_index", [1, 5, 11])
def test_add_to_compare(browser, url, product_index, wait):
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
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#compare-total')))
    button.click()
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#content tbody tr strong')))
    second_compare_product = browser.find_elements_by_css_selector('#content tbody tr strong')[1].text
    assert second_compare_product == second_product_name


# Тест клика по #column-left > div.list-group на Desktops что мы точно на Desktops по тексту #content > h2
@pytest.mark.parametrize("catalog_id", [20, 34, 18])
def test_catalog_name(browser, url, catalog_id, wait):
    catalog_page_url = url + f'/index.php?route=product/category&path=' + str(catalog_id)
    browser.get(catalog_page_url)
    catalog_name = browser.find_element_by_css_selector('#content h2').text
    other_catalog_list = browser.find_element_by_css_selector('.list-group')
    other_catalog_list.find_element_by_partial_link_text(catalog_name).click()
    new_catalog_name = browser.find_element_by_css_selector('#content h2').text
    assert new_catalog_name == catalog_name
