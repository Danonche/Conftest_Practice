from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_basket(browser):
    browser.get(link)
    time.sleep(5)
    button = None
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    assert button, "!!---no item (:---!!"
 