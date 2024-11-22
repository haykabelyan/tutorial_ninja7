from pages.CartPage import CartPage
import allure
import pytest

@allure.feature('Shopping Cart')
@allure.suite('Product Operations')
@allure.title('Add MacBook to Cart')
@allure.description('This test verifies that a MacBook can be successfully added to the shopping cart.')
@allure.severity('critical')
@pytest.mark.smoke
def test_add_to_cart(driver):
    with allure.step('Open Cart Page'):
        cart_page = CartPage(driver)
        cart_page.open()

    with allure.step('Add Product to Cart'):
        cart_page.add_product_to_cart()

    with allure.step('Verify Success Message and Cart Update'):
        assert "Success: You have added" in cart_page.get_success_message()

    with allure.step('Wait for the item to appear in the cart'):
        cart_page.wait_for_the_item_to_appear_in_the_cart(1)

    with allure.step('Verify Product in Cart'):
        cart_page.open_cart()
        assert 'MacBook' in cart_page.get_cart_contents()

