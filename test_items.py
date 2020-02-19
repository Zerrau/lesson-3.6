from selenium import webdriver
import time
import unittest
import pytest


class SubclassesTest(unittest.TestCase):
    def test_One(self):
        try:
            link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
            browser = webdriver.Chrome()
            browser.get(link)
        finally:
            time.sleep(3)
            browser.quit()


if __name__ == '__main__':
    unittest.main()
