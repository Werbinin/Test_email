import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

@pytest.fixture
def get_webdriver():
    options = chrome_options