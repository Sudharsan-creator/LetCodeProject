from selenium.webdriver.common.by import By


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    # A single web element using the provided locator
    def find(self, *locator):
        return self.driver.find_element(*locator)

    # Click on the element found by the locator
    def click(self, locator):
        self.find(*locator).click()

    # Clear the input field and set it with the given value
    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)






