import random
import time
import pytest
from Pages.Locators import flipkart
from Drivers.browser import driver
from pytest_bdd import when, given, then, scenario, parsers
from selenium.webdriver.support.ui import Select
from Source.conftest import wait_and_send, wait_and_click, wait_till_element_present


brand_name = "NIKE"


@pytest.mark.search()
@scenario('../Features/test_flipkart.feature', 'Search for any item within flipkart website')
def test_search():
    pass


@pytest.mark.filters()
@scenario('../Features/test_flipkart.feature', 'Applying filters on search results')
def test_filters():
    pass


@pytest.mark.buy()
@scenario('../Features/test_flipkart.feature', 'To verify user is able to choose size and buy the product')
def test_buy_now():
    pass


@given("User navigates to flipkart homepage")
def initialize_test():
    pass                                            #Since we are already using a pre-test function in conftest.py file


@when(parsers.parse("User searches for {item}"))
def search_bar(item):
    wait_and_send("xpath", flipkart.txt_search_bar, item)
    wait_and_click("xpath", flipkart.btn_search)


@then(parsers.parse("User verifies all the items related to the {function} is displayed as result"))
def verify_result(function):
    wait_till_element_present("xpath", flipkart.result_bread_crumbs)
    if function == "search":
        category = driver.find_elements_by_xpath(flipkart.result_bread_crumbs)
        assert "Footwear" in category[-1].text
    elif function == "filter":
        time.sleep(3)
        brand = driver.find_elements_by_xpath(flipkart.filter_assert)           #List of brand names
        price = driver.find_elements_by_xpath(flipkart.price_assert)            #List of price for each item
        if (len(brand) != 0):
            pos = random.randint(1, 10)                            # Randomly select any product
            assert brand[pos].text == brand_name
            rate = (price[pos].text)
            rate = rate.replace('₹', '')
            rate = rate.replace(',', '')
            assert int(rate) <= 2000                                 #Asserting applied filters


@then("User applies filter to sort out the result")
def filters():
    wait_and_send("xpath", flipkart.filter_search, brand_name)              #applying brand name filter
    wait_and_click("xpath", flipkart.filter_checkbox)
    wait_till_element_present("xpath", flipkart.filter_section)
    time.sleep(3)
    select = Select(driver.find_element_by_xpath(flipkart.max_drp_down_filter))     #applying price range filter
    select.select_by_value("2000")
    wait_till_element_present("xpath", flipkart.filter_section)


@then("User select any item and choose any available size")
def choose_item():
    wait_and_click("xpath", flipkart.Any_element)
    driver.switch_to.window(driver.window_handles[1])                   # Switch to the new window
    wait_till_element_present("xpath", flipkart.specs)
    specs = driver.find_elements_by_xpath(flipkart.specs)
    if len(specs) == 1:
        List = driver.find_elements_by_xpath(flipkart.size_list.format(1))            #Get list of all available sizes
    else:
        List = driver.find_elements_by_xpath(flipkart.size_list.format(2))
    if (len(List) != 0):
        pos = random.randint(0, len(List))                              #Randomly select any size value
        List[pos].click()


@then("User clicks on buy now option and is navigated to login page")
def buy_and_login():
    wait_and_click("xpath", flipkart.btn_proceed_to_buy)
    wait_till_element_present("xpath", flipkart.login_header)

