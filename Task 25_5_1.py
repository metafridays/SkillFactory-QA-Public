import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_petfriends(web_browser):

    # Open PetFriends base page:
    web_browser.get("https://petfriends1.herokuapp.com/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()
    
    # click existing user button
    btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()


    # add email
    field_email = web_browser.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("taroso1031@vy89.com")
    
    # add password
    field_pass = web_browser.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("123456")
    
    # click submit button
    btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()


    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if web_browser.current_url == 'https://petfriends1.herokuapp.com/all_pets':
        # Make the screenshot of browser window:
        web_browser.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/metaf/Documents/QA/chromedriver/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('taroso1031@vy89.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   
   

   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0