#Тест добавления в Cart
#Тест Like #u_0_1 > button > span
#Тест написания ревью #input-name
#Тест совпадения названия с название сверху #product-product > ul > li:nth-child(3) > a

#Тест добавляя в Wish list
def test_add_wish_list(browser, url)
    browser.get(url)
    featured_product = browser.find_elements_by_css_selector('.product-layout')[0]
    product_name = featured_product.find_element_by_css_selector('.caption h4 a').text