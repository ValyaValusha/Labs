# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Valya")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("kissme")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("kissme777fff")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("kissme777fff777")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("kissme")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("kissme777")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
        self.assertIn("Python", driver.title)
        driver.find_element_by_xpath("//div[3]/div/div/a/img").click()
        driver.find_element_by_id("number").clear()
        driver.find_element_by_id("number").send_keys("55")
        driver.find_element_by_id("submit_btn").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
