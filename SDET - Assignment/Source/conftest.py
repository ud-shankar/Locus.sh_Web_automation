import pytest
from Drivers.browser import driver
from Pages.Locators import flipkart
from pytest_bdd import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)


@pytest.fixture(scope="function", autouse=True)
def pretest():                                                      #Pre-test which will run before every test function
    flipkart_home_page()
    yield driver
    wait_and_click("xpath", flipkart.img_filpkart)


@pytest.fixture(scope="session", autouse=True)
def posttest():                                                     #teardown at the end of every session
    yield driver
    driver.quit()


def flipkart_home_page():
    driver.get("https://www.flipkart.com/")
    if len(driver.find_elements_by_xpath(flipkart.window_pop_up)) > 0:              #Handle initial pop up message
        wait_and_click("xpath", flipkart.btn_pop_up_close)
    else:
        pass


@when("User is in home page")
def home_assert():
    assert driver.find_element_by_xpath(flipkart.top_bar).is_displayed()


def wait_and_click(locator_type, element):
    if locator_type == "id":
        wait.until(EC.element_to_be_clickable((By.ID, element))).click()
    elif locator_type == "xpath":
        wait.until(EC.element_to_be_clickable((By.XPATH, element))).click()


def wait_and_send(locator_type, element, text):
    if locator_type == "id":
        wait.until(EC.element_to_be_clickable((By.ID, element))).send_keys(text)
    elif locator_type == "xpath":
        wait.until(EC.element_to_be_clickable((By.XPATH, element))).send_keys(text)


def wait_till_element_present(locator_type, element):
    if locator_type == "id":
        wait.until(EC.presence_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        wait.until(EC.presence_of_element_located((By.XPATH, element)))
