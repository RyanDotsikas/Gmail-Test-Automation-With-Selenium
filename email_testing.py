from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import random

def load_inbox():

	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://gmail.com')
	
	
	email_element = driver.find_element_by_css_selector(".whsOnd.zHQkBf")
	email_element.send_keys("dogwizard69")

	next_button = driver.find_element_by_css_selector(".RveJvd.snByac")
	next_button.click()
	time.sleep(2)

	password_element = driver.find_element_by_css_selector(".whsOnd.zHQkBf")
	password_element.send_keys("ter12wvrrahah")


	next_button = driver.find_element_by_css_selector(".RveJvd.snByac")
	next_button.click()

	time.sleep(5) # wait to load next

	return driver

def send_mail(driver, recipient_address, email_subject, path_to_file):

	create_mail_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3")
	create_mail_button.click()

	to_field = driver.find_element_by_css_selector(".vO")
	to_field.send_keys(recipient_address)

	subject_field = driver.find_element_by_css_selector(".aoT")
	subject_field.send_keys(email_subject)

	emailbody_field = driver.find_element_by_css_selector(".Am.Al.editable.LW-avf")
	emailbody_field.send_keys("Yarr harr I am an email spam bot ayy lmao " + str(random.randint(1,1000)))
	time.sleep(3)

	# attachment_button = driver.find_element_by_css_selector(".a1.aaA.aMZ")
	# attachment_button.click()
	# time.sleep(5)
	# attachment_button.send_keys(path_to_file)

	send_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3")
	send_button.click()

driver = load_inbox()

send_mail(driver, "matthew.caminiti@mail.mcgill.ca", "First Test", (os.getcwd() + '/chicken.jpg'))


