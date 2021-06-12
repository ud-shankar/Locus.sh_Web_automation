import random
import time
import pytest
from Pages.Locators import flipkart
from Drivers.browser import driver
from pytest_bdd import when, given, then, scenario, parsers
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
    else:
        wait_till_element_present("xpath", flipkart.filter_section)
        time.sleep(3)
        filter = driver.find_elements_by_xpath(flipkart.filter_assert)
        if (len(filter) != 0):
            pos = random.randint(0, len(filter))                            # Randomly select any product
            assert filter[pos].text == brand_name


@then("User applies filter to sort out the result")
def filters():
    wait_and_send("xpath", flipkart.filter_search, brand_name)
    wait_and_click("xpath", flipkart.filter_checkbox)


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

