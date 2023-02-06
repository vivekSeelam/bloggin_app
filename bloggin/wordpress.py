from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

import time

class WordPress:

    def __init__(self):
        self.driver = None
        self.blog_url = "https://hangryowl.wordpress.com/"
        logging.info("Initialised the wordpress class")
        

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get(self.blog_url)
        time.sleep(10)
        xpath_login = "//a[contains(text(), 'Log in')]"
        self.driver.find_element(by=By.XPATH,value=xpath_login).click()
        

        xpath_email_field = "//input[@id='usernameOrEmail']"
        # TODO: keep the userid and password somewhere safe and not hardcode them
        self.driver.find_element(by=By.XPATH,value=xpath_email_field).send_keys(username)

        xpath_continue_butt = "//button[contains(text(),'Continue')]"
        self.driver.find_element(by=By.XPATH,value=xpath_continue_butt).click()

        time.sleep(2)

        xpath_password_field = "//input[@id='password']"
        # TODO: keep the userid and password somewhere safe and not hardcode them
        self.driver.find_element(by=By.XPATH,value=xpath_password_field).send_keys(password)

        xpath_continue_butt = "//button[contains(text(),'Log In')]"
        self.driver.find_element(by=By.XPATH,value=xpath_continue_butt).click()

        time.sleep(5)

    def update_text(self,title, text):
        xpath_write_butt = "//span[contains(text(),'Write')]"
        self.driver.find_element(by=By.XPATH,value=xpath_write_butt).click()
        # write_button_click = """document.getElementsByClassName("ab-item")[5].click()"""
        # self.driver.execute(write_button_click)


        self.driver.implicitly_wait(10)

        # This took a fucking lot of time and clearly a little obvious

        iframe_xpath = """//iframe[@class="is-loaded"]"""
        iframe = self.driver.find_element(by=By.XPATH, value=iframe_xpath)
        self.driver.switch_to.frame(iframe)

        self.driver.implicitly_wait(10)
        time.sleep(20)

        changing_title_script = f"""document.getElementsByClassName("wp-block wp-block-post-title block-editor-block-list__block editor-post-title editor-post-title__input rich-text")[0].innerHTML = "{title}";"""
        self.driver.execute_script(changing_title_script)

        time.sleep(5)

        click_on_text_box = """document.getElementsByClassName("editor-post-text-editor")[0].focus()"""
        self.driver.execute_script(click_on_text_box)

        time.sleep(2)
        text_box_xpath = """//textarea[@class="editor-post-text-editor"]"""
        self.driver.find_element(by=By.XPATH,value=text_box_xpath).send_keys(f"{text}")

        time.sleep(15)

    def publish(self):
        clicking_publish_butt_js = """document.getElementsByClassName("components-button editor-post-publish-panel__toggle editor-post-publish-button__button is-primary")[0].click()"""
        self.driver.execute_script(clicking_publish_butt_js)

        time.sleep(15)
        sec_clicking_publish_butt_js = """document.getElementsByClassName("components-button editor-post-publish-button editor-post-publish-button__button is-primary")[0].click()"""
        self.driver.execute_script(sec_clicking_publish_butt_js)

        time.sleep(10)
    
    def close_the_window(self):
        self.driver.close()






