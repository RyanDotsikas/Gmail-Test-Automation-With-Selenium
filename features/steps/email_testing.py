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
	driver.implicitly_wait(15)

	return driver

#"dogwizard69"
#"ter12wvrrahah"
def load_inbox(driver, username, password):
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
		while(True): # repeatedly try to press the send button in case of oversized file upload
			try:
				send_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3")
				send_button.click()
				break		
			except Exception as e:
				continue
	except Exception as e:
		print("Error: %s" % e)
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

def check_invalid_email(driver):
	# driver = setup_webdriver()
	# load_inbox(driver, "dogwizard69", "ter12wvrrahah")

	body = driver.find_element_by_css_selector(".y2").text
	while("Address not found" not in body):
		refresh_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.nu.T-I-ax7.L3")
		refresh_button.click()
		try:
			body = driver.find_element_by_css_selector(".y2").text
		except Exception as e:
			pass
		
	return True
	# if("Address not found" in body):
	# 	return True
	# else:
	# 	return False

def check_oversized_attachment(driver, attachment_name):
	driver = setup_webdriver()
	load_inbox(driver, "dogwizard69", "ter12wvrrahah")

	body = driver.find_element_by_css_selector(".y2").text
	if(attachment_name == body[3:].split()[0]):
		return True
	else:
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

	email = {}
	email["delivery_address"] = "dogwizard69@gmail.com"
	email["recipient_address"] = recipient_address
	email["email_subject"] = email_subject
	email["attachment_names"] = []

	for path in paths_to_attachments:
		attach_file(driver, path)
		email["attachment_names"].append(path.split("/")[len(path.split("/")) - 1])

	press_send(driver)

	while(True):
		if(check_sent_popup(driver)):
			break

	driver.quit()
	return email

def check_sent_mail(driver, receiver_address, email, multi_attach = False, oversized = False):
	# driver = setup_webdriver()
	# load_inbox(driver, "dogwizard69", "ter12wvrrahah") # currently using same email account to test

	search_box = driver.find_element_by_css_selector(".gb_1e")
	search_box.send_keys("in:sent\n")
	
	# wait = WebDriverWait(driver, 10)
	# refresh_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'T-I') and contains(@class, 'J-J5-Ji') and contains(@class, 'nu') and contains(@class, 'T-I-ax7') and contains(@class, 'L3')]")))

	refresh_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.nu.T-I-ax7.L3")
	refresh_button.click()
	
	if(oversized):
		emails_table = driver.find_element_by_css_selector(".F.cf.zt")
		while(True):
			top_email = emails_table.find_element_by_css_selector(".zA.zE")
			top_email.click()

			# found_attach_name = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aQv.T-I-ax7.L3").get_attribute("aria-label").split()
			# found_attach_name = found_attach_name[len(found_attach_name) - 1]
			found_attach_name = driver.find_element_by_xpath("//a/span[@dir='ltr']").text
			print("eat my ass %s" % found_attach_name)
			if(not multi_attach):
				if(found_attach_name != email["attachment_name"]):
					back_button = driver.find_element_by_css_selector(".T-I.J-J5-Ji.lS.T-I-ax7.mA.T-I-Zf-aw2")
					back_button.click()
				else:
					return True
					break


	# to_text = driver.find_element_by_css_selector(".yW").text
	to_text = driver.find_element_by_xpath("//div[contains(@class, 'BltHke') and contains(@class, 'nH') and contains(@class, 'oy8Mbf')]/div/div/div/table/tbody/tr/td[contains(@class, 'yX') and contains(@class, 'xY')]/div[@class='yW']").text
	if(len(to_text.split()) == 2):
		to_text = to_text.split()[1]
	

	# subject_text = driver.find_element_by_css_selector(".y6").text
	subject_text = driver.find_element_by_xpath("//div[contains(@class, 'BltHke') and contains(@class, 'nH') and contains(@class, 'oy8Mbf')]/div/div/div/table/tbody/tr/td[contains(@class, 'xY') and contains(@class, 'a4W')]/div[@class='xS']/div[@class='xT']/div[@class='y6']").text

	# body_text = driver.find_element_by_css_selector(".y2").text
	body_text = driver.find_element_by_xpath("//div[contains(@class, 'BltHke') and contains(@class, 'nH') and contains(@class, 'oy8Mbf')]/div/div/div/table/tbody/tr/td[contains(@class, 'xY') and contains(@class, 'a4W')]/div[@class='xS']/div[@class='xT']").text
	print(body_text)
	# body_text = body_text.split('-')[1].strip()


	# body_text = body_text[4:]

	if(multi_attach):
		while(True):
			if(len(driver.find_elements_by_css_selector(".F.cf.zt")) == 1):
				continue
			else:
				break
		emails_table = driver.find_elements_by_css_selector(".F.cf.zt")[1]
		top_email = emails_table.find_element_by_css_selector(".zA.zE.byw")
		top_email = emails_table.find_element_by_css_selector(".zA.zE")
		top_email.click()

		attachment_names = driver.find_element_by_css_selector(".f.gW").get_attribute("title").split(',')
		attachment_names = [str(f.strip()) for f in attachment_names]

		email["attachment_names"].sort()
		attachment_names.sort()
		print("email attachment names: %s" % email["attachment_names"])
		print("found attachment names: %s" % attachment_names)

		if(email["attachment_names"] != attachment_names):
			print("Attachment names not the same")
			return False
		if(email["delivery_address"] == email["recipient_address"]):
			if(to_text != "me"):
				return False
		elif(email["recipient_address"] != to_text):
			return False
		if(email["email_subject"] != subject_text):
			return False

		return True
	else:
		attach_text = driver.find_element_by_css_selector(".brc").get_attribute("title")
		print("to_text [%s]" % to_text)
		print("subject text [%s]" % subject_text)
		print("body text [%s]" % body_text)
		print("attach text [%s]" % attach_text)
		if(email["attachment_name"] in body_text): # oversized check
			return True
		else:
			print(body_text)
		if(email["delivery_address"] == email["recipient_address"]):
			if(to_text != "me"):
				return False
		elif(email["recipient_address"] != to_text):
			return False
		if(email["email_subject"] != subject_text):
			return False
		if(email["attachment_name"] != attach_text):
			return False

		return True

# email : dictionary containing delivery_address, recipient_address, email_subject, attachment_name
# returns boolean of whether or not email is in the inbox
def receive_mail(receiver_address, email, multi_attach = False):
	driver = setup_webdriver()
	load_inbox(driver, "dogwizard69", "ter12wvrrahah") # currently using same email account to test

	try:
		while(True):
			sender = driver.find_element_by_css_selector(".zF").get_attribute("email")
			if sender:
				break

		body = driver.find_element_by_css_selector(".y2").text
		subjects = driver.find_elements_by_css_selector(".bqe")
		subject = subjects[1].text

		email_button = driver.find_element_by_css_selector(".zA.zE.byw")
		email_button.click()

		# possible inconsistency with timing here
		# body = driver.find_element_by_css_selector(".a3s.aXjCH").text

		attachment_name = ""
		attachment_names = []
		if(multi_attach):
			attachment_names = driver.find_element_by_css_selector(".f.gW").get_attribute("title").split(',')
			attachment_names = [f.strip() for f in attachment_names]

			email["attachment_names"].sort()
			attachment_names.sort()
			
			if(email["attachment_names"] != attachment_names):
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


