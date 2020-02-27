from selenium import webdriver
import time
import unittest


# import pytest


class SubclassesTest(unittest.TestCase):
    def test_One(self):
        try:
            link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
            browser = webdriver.Chrome()
            browser.get(link)
            browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button').click()
            browser.find_element_by_xpath('//*[@id="messages"]/div[3]/div/p[2]/a[1]').click()
            book = browser.find_element_by_xpath('//*[@id="basket_formset"]/div/div/div[2]/h3/a')  # Coders at Work
            assert book.text == 'Coders at Work', 'Book title not found'
            get_value = browser.find_element_by_xpath('//*[@id="id_form-0-quantity"]').get_attribute("value")  # value 1
            assert get_value == '1', 'Wrong amount of books'
            price = browser.find_element_by_xpath('//*[@id="basket_formset"]/div/div/div[4]/p')  # price £19.99
            assert price.text == '£19.99', 'Wrong book price'
        finally:
            browser.quit()


if __name__ == '__main__':
    unittest.main()
