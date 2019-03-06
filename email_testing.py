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
	time.sleep(2) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	password_element = driver.find_element_by_css_selector(".whsOnd.zHQkBf")
	password_element.send_keys("ter12wvrrahah")


	next_button = driver.find_element_by_css_selector(".RveJvd.snByac")
	next_button.click()

	time.sleep(5) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	return driver

def send_mail(recipient_address, email_subject, path_to_attachment):
	driver = load_inbox()
	
	create_mail_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3")
	create_mail_button.click()

	to_field = driver.find_element_by_css_selector(".vO")
	to_field.send_keys(recipient_address)

	subject_field = driver.find_element_by_css_selector(".aoT")
	subject_field.send_keys(email_subject)

	emailbody_field = driver.find_element_by_css_selector(".Am.Al.editable.LW-avf")
	emailbody_field.send_keys("Yarr harr I am an email spam bot ayy lmao " + str(random.randint(1,1000)))
	time.sleep(3) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	file_entry = driver.find_element_by_name("Filedata")
	file_entry.send_keys(path_to_attachment)
	time.sleep(1) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	send_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3")
	send_button.click()
	time.sleep(2) # NEED TO FIGURE OUT PROPER WAIT FOR LOAD

	email = {}
	email["delivery_address"] = "dogwizard69@gmail.com"
	email["recipient_address"] = recipient_address
	email["email_subject"] = email_subject
	email["attachment_name"] = path_to_attachment.split("/")[len(path_to_attachment.split("/")) - 1]

	driver.quit()
	return email

# email : dictionary containing delivery_address, recipient_address, email_subject, attachment_name
# returns boolean of whether or not email is in the inbox
def receive_mail(receiver_address, email):
	driver = load_inbox() # currently using same email account to test

	try:
		received_email = driver.find_element_by_css_selector(".afn")
		subject = driver.find_element_by_css_selector(".bqe")
		email_info = received_email.text
		print(subject)

		# OLD code block trying to get text of WebElement ---------
		# email_info = driver.execute_script('''
		# var parent = arguments[0];
		# var child = parent.firstChild;
		# var ret = "";
		# while(child) {
		# 	if(child.nodeType === Node.TEXT_NODE)
		# 		ret += child.textContent;
		# 	child = child.nextSibling;
		# }
		# return ret;
		# ''', received_email).split(',')
		# END OLD --------

		print("Email info %s" % email_info)
		if(email_info[2] == email["email_subject"]):
			return True
	except Exception as e:
		print("Bricked trying to find received email: [%s]" % e)
		return False

	print("No match on email subject")
	driver.quit()
	return False

email = send_mail("dogwizard69@gmail.com", "First Test", (os.getcwd() + '/images/chicken.jpg'))

success = receive_mail("dogwizard69@gmail.com", email)

print("Received Email Check: %s\a" % success)

