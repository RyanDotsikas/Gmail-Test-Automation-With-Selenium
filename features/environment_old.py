from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.implicitly_wait(15)
	driver.get('https://gmail.com')
	context.driver = driver

def after_all(context):
	context.driver.quit()
