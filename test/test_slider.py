from pages.SliderPage import SliderPage
import pytest


@pytest.mark.regression
def test_slider_functionality(driver):
    slider_page = SliderPage(driver)
    slider_page.open()
    first_slide_src = slider_page.get_active_slide_src()
    slider_page.click_next_slide()
    slider_page.wait_for_slide_change(first_slide_src)
    second_slide_src = slider_page.get_active_slide_src()
    assert first_slide_src != second_slide_src

    slider_page.click_prev_slide()
    slider_page.wait_for_slide_change(second_slide_src)
    reverted_slide_src = slider_page.get_active_slide_src()

    assert reverted_slide_src == first_slide_src

