import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def launchbrowser():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    driver.quit()


@pytest.fixture(scope="class")
def launchbrowserclass(request):
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    request.cls.driver.quit()


def test_printURL(launchbrowser):
    driver.get("https://www.payopic.com/")


def test_printURL1(launchbrowser):
    driver.get("https://www.payopic.com/")
    print(driver.current_url)


def test_printURL2(launchbrowser):
    driver.get("https://pypi.org/project/pytest-html/")
    time.sleep(2)
    screen = driver.find_element(By.XPATH, "//span[text()='Latest version']")
    screen.click()
    time.sleep(1)

    def screenshot(screen2):
        time.sleep(1)
        #driver.save_screenshot(screen2)
        driver.save_screenshot(r'C:\Users\sudharsan\Desktop\screenshot\screenshot.png')

        print("screenshot saved successfully")

    screenshot(r'C:\Users\sudharsan\Desktop\screenshot\screenshot.png')


@pytest.mark.usefixtures("launchbrowserclass")
class Test_payopic:
    def test_enterUrl(self):
        self.driver.get("https://www.payopic.com/")
