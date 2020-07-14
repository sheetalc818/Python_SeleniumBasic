import pytest

pytest
from selenium import webdriver


class BaseTest:
    @pytest.fixture
    def launching_webdriver(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        baseTest = BaseTest()
        baseTest.launching_webdriver()
