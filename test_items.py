link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_form(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form"))

    assert button > 0, "The button is missing"
