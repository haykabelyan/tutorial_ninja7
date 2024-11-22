from pages.SearchPage import SearchPage
import allure
import pytest

@allure.feature('Product Search')
@allure.suite('Search Functionality')
@allure.title('Search for MacBook Product')
@allure.description('This test verifies the search functionality by searching for a MacBook and checking that the search results are filtered correctly.')
@pytest.mark.smoke
def test_search_product(driver):
    with allure.step('Open Search Page'):
        search_page = SearchPage(driver)
        search_page.open()

    with allure.step('Search for Product'):
        search_page.search_product('MacBook')

    with allure.step('Get Search Results'):
        products = search_page.get_search_results()

    with allure.step('Check All Products are MacBooks'):
        filtered_products = [text for text in products if 'MacBook' in text]
        assert len(products) == len(filtered_products), "Not all products in the search results are MacBook."



