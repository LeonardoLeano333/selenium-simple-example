"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# download from http://chromedriver.storage.googleapis.com/index.html?path=2.14/
CHROME_PATH = "C:\\Users\\Dell\\Downloads\\chromedriver.exe"
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        """
        function which runs in the beggining of each test
        """
        self.driver = webdriver.Chrome(
            executable_path=CHROME_PATH
            )

    def tearDown(self):
        """
        function which runs in the end of each test
        """
        self.driver.close()

    def test_search_in_python_org(self):
        """
        example of test getting information from python website
        """
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


if __name__ == "__main__":
    unittest.main()