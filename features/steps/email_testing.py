from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import random

def setup_webdriver():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.implicitly_wait(10)

	return driver

#"dogwizard69"
#"ter12wvrrahah"
def load_inbox(driver, username, password):
	#driver = webdriver.Chrome(ChromeDriverManager().install())
	#driver.implicitly_wait(10)
	driver.get('https://gmail.com')
	
	email_element = driver.find_element_by_css_selector(".whsOnd.zHQkBf[autocomplete='username']")
	email_element.send_keys(username)

	next_button = driver.find_element_by_css_selector(".RveJvd.snByac")
	next_button.click()

	password_element = driver.find_element_by_css_selector(".whsOnd.zHQkBf[autocomplete='current-password']")
	password_element.send_keys(password)

	wait = WebDriverWait(driver, 10) # will repeatedly search for element until it is clickable, max search time is 10 sec
	next_button = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='passwordNext']/content/span")))
	next_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='passwordNext']/content/span")))
	next_button.click()

	#return driver

def click_create_mail(driver):
	try:
		create_mail_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3")
		create_mail_button.click()
		return True
	except Exception as e:
		return False
	
def fill_to_field(driver, recipient_address):
	try:
		to_field = driver.find_element_by_css_selector(".vO")
		to_field.send_keys(recipient_address)
		return True
	except Exception as e:
		return False
	
def fill_subject_field(driver, subject):
	try:
		subject_field = driver.find_element_by_css_selector(".aoT")
		subject_field.send_keys(subject)
		return True
	except Exception as e:
		return False

def fill_body_field(driver, body):
	try:
		emailbody_field = driver.find_element_by_css_selector(".Am.Al.editable.LW-avf")
		emailbody_field.send_keys(body + " " + str(random.randint(1,10000)))
		return True
	except Exception as e:
		return False

def attach_file(driver, path):
	try:
		file_entry = driver.find_element_by_name("Filedata")
		file_entry.send_keys(path)
		return True
	except Exception as e:
		return False

def press_send(driver):
	try:
		send_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3")
		send_button.click()
	except Exception as e:
		return False

def check_sent_popup(driver):
	try:
		popup = driver.find_element_by_css_selector(".bAq").text
		if(popup == "Message sent."):
			return True
		else:
			return False
	except Exception as e:
		# print("Bricked getting popup text [%s]" % e)
		return False


def send_mail(recipient_address, email_subject, path_to_attachment):
	driver = setup_webdriver()
	load_inbox(driver, "dogwizard69", "ter12wvrrahah")

	click_create_mail(driver)

	fill_to_field(driver, recipient_address)

	fill_subject_field(driver, email_subject)

	fill_body_field(driver, "Yarr harr I am an email spam bot ayy lmao " + str(random.randint(1,1000)))

	attach_file(driver, path_to_attachment)

	press_send(driver)

	while(True):
		if(check_sent_popup(driver)):
			break

	email = {}
	email["delivery_address"] = "dogwizard69@gmail.com"
	email["recipient_address"] = recipient_address
	email["email_subject"] = email_subject
	email["attachment_name"] = path_to_attachment.split("/")[len(path_to_attachment.split("/")) - 1]

	driver.quit()
	return email

def send_mail_multi_attach(recipient_address, email_subject, paths_to_attachments):
	driver = setup_webdriver()
	load_inbox(driver, "dogwizard69", "ter12wvrrahah")

	click_create_mail(driver)

	fill_to_field(driver, recipient_address)

	fill_subject_field(driver, email_subject)

	fill_body_field(driver, "Yarr harr I am an email spam bot ayy lmao " + str(random.randint(1,1000)))
	# time.sleep(3) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	email = {}
	email["delivery_address"] = "dogwizard69@gmail.com"
	email["recipient_address"] = recipient_address
	email["email_subject"] = email_subject
	email["attachment_names"] = []

	for path in paths_to_attachments:
		attach_file(driver, path)
		# time.sleep(1) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD
		email["attachment_names"].append(path.split("/")[len(path.split("/")) - 1])

	press_send(driver)
	# time.sleep(2) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	while(True):
		if(check_sent_popup(driver)):
			break

	driver.quit()
	return email

# email : dictionary containing delivery_address, recipient_address, email_subject, attachment_name
# returns boolean of whether or not email is in the inbox
def receive_mail(receiver_address, email, multi_attach = False):
	driver = setup_webdriver()
	load_inbox(driver, "dogwizard69", "ter12wvrrahah") # currently using same email account to test

	try:
		sender = driver.find_element_by_css_selector(".zF").get_attribute("email")
		body = driver.find_element_by_css_selector(".y2").text

		subjects = driver.find_elements_by_css_selector(".bqe")
		subject = subjects[1].text

		email_button = driver.find_element_by_css_selector(".zA.zE.byw")
		email_button.click()
		# time.sleep(1) # NEED TO FIO WAIT FOR LOAD

		# TODO : CLEAN UP EMAIL CHECKING TIMING!
		body = driver.find_element_by_css_selector(".a3s.aXjCH").text

		attachment_name = ""
		attachment_names = []
		if(multi_attach):
			attachment_names = [f.get_attribute("title") for f in driver.find_elements_by_css_selector(".f.gW")]
			sorted_known_attach_names = email["attachment_names"].sort()
			sorted_found_attach_names = attachment_names.sort()
			if(sorted_known_attach_names != sorted_found_attach_names):
				print("Attachment names not the same")
				return False
			if(subject == email["email_subject"]):
				return True
		else:
			attachment_name = driver.find_element_by_css_selector(".f.gW").get_attribute("title")
			if(attachment_name == email["attachment_name"] and subject == email["email_subject"]):
				return True
	except Exception as e:
		print("Bricked trying to find received email: [%s]" % e)
		return False

	print("No match on email content")
	driver.quit()
	return False

# email = send_mail("dogwizard69@gmail.com", "Second Test", (os.getcwd() + '/images/chicken.jpg'))
# email = send_mail_multi_attach("dogwizard69@gmail.com", "Second Test", [(os.getcwd() + '/images/chicken.jpg'), (os.getcwd() + '/images/tomato.jpeg')])
# email = {"delivery_address" : "dogwizard69@gmail.com", "recipient_address" : "dogwizard69@gmail.com", "email_subject" : "Second Test", "attachment_name" : "chicken.jpg"}
# success = receive_mail("dogwizard69@gmail.com", email, True)

# print("Received Email Check: %s\a" % success)

