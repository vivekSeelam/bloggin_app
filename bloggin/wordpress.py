from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Firefox()
blog_url = "https://hangryowl.wordpress.com/"
driver.get(blog_url)

xpath_login = "//a[contains(text(), 'Log in')]"
driver.find_element(by=By.XPATH,value=xpath_login).click()

xpath_email_field = "//input[@id='usernameOrEmail']"
driver.find_element(by=By.XPATH,value=xpath_email_field).send_keys("vivektheseal")

xpath_continue_butt = "//button[contains(text(),'Continue')]"
driver.find_element(by=By.XPATH,value=xpath_continue_butt).click()

time.sleep(2)

xpath_password_field = "//input[@id='password']"
driver.find_element(by=By.XPATH,value=xpath_password_field).send_keys("Surekha123#")

xpath_continue_butt = "//button[contains(text(),'Log In')]"
driver.find_element(by=By.XPATH,value=xpath_continue_butt).click()

xpath_write_butt = "//span[contains(text(),'Write')]"
driver.find_element(by=By.XPATH,value=xpath_write_butt).click()

print("here we are ")
print("lets see")