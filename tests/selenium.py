from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = FirefoxService(executable_path=r"C:\Users\USER\geckodriver.exe")
        
        #Firefox location
        firefox_options = FirefoxOptions()
        firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" 
        
        cls.selenium = webdriver.Firefox(service=service, options=firefox_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_homepage(self):
        self.selenium.get(f'{self.live_server_url}')
        assert 'Catgeram' in self.selenium.title

