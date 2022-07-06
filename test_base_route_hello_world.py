from audioop import reverse
from http import client

import requests as requests
import response

import pytest
from scipy.sparse import data
from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    dc = {
            "browserName": "chrome",
            "platformName": "Windows 11"

         }

    # selenium grid standAlone headless
    # driver = webdriver.Remote("http://localhost:4444",desired_capabilities= dc,options=chrome_options)

    #selenium grid standAlone
    driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    yield driver
    driver.close()


def test_message(driver):
    driver.get('http://localhost:5000/')
    message=driver.find_element(By.CSS_SELECTOR,"body").text
    assert  message== "Welcome to the Application with updated code!"

def test_response(driver):
    driver.get('http://localhost:5000/')
    response = requests.get("http://localhost:5000")
    status = response.status_code
    assert status == 200


def test_message(driver):
    driver.get('http://localhost:5000/stub')
    message=driver.find_element(By.CSS_SELECTOR,"body").text
    assert  message== "Value of Stub: 200"

def test_response(driver):
    driver.get('http://localhost:5000/stub')
    response = requests.get("http://localhost:5000/stub")
    status = response.status_code
    assert status == 200



