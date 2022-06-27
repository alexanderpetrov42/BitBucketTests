import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LogInPage

class testSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.loginpage = LogInPage(self.driver)
        self.loginpage.open_page_and_search(self)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == self.driver.current_url

    def test_login_with_valid_data_bitbucket(self):
        self.loginpage = LogInPage(self.driver)
        self.loginpage.login(self)
        self.assertTrue(self.loginpage.is_logged_in());

    if __name__ == "__main__":
        unittest.main()