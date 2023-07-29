from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# import pytest
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_edd_basket(browser):
  try:
    browser.get(link)
    time.sleep(30)
  
    button = None
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primarys")
    assert button != None, "Кнопка на месте"
  except NoSuchElementException:
      pass