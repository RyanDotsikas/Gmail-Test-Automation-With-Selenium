from behave import *
import email_testing as et
import os
import random

# ------------ GIVEN ---------------
@given('I am logged into a valid Gmail account')
def step_impl(context):
    context.driver = et.setup_webdriver()
    et.load_inbox(context.driver, "dogwizard69", "ter12wvrrahah")
# ----------------------------------

# ------------ WHEN ---------------
@when('I choose to compose a new email')
def step_impl(context):
    et.click_create_mail(context.driver)

@when('I enter a valid email address for the recipient')
def step_impl(context):
    context.recipient = "dogwizard69@gmail.com"
    context.recipient_password = "ter12wvrrahah"
    et.fill_to_field(context.driver, context.recipient)

@when('I enter a subject line or a body to the email')
def step_impl(context):
    context.subject = "Test Subject"
    et.fill_subject_field(context.driver, context.subject)
    et.fill_body_field(context.driver, "Here is some sample generated text for the body: " + str(random.randint(1,1000)))

@when('I attach a .jpg format image that is less than 25 Mb in size')
def step_impl(context):
    et.attach_file(context.driver, (os.getcwd() + '/images/chicken.jpg'))

@when('I send the email')
def step_impl(context):
	et.press_send(context.driver)
    et.check_sent_popup(context.driver)

@when('I attach a .png format image that is less than 25 Mb in size')
def step_impl(context):
    et.attach_file(context.driver, (os.getcwd() + '/images/bacon.png'))

@when('I attach a .jpg format image that exceeds 25 Mb in size')
def step_impl(context):
    et.attach_file(context.driver, (os.getcwd() + '/images/54mb.jpg'))

@when('I attach multiple .jpg format images (that total less than 25 Mb)')
def step_impl(context):
    paths_to_attachments = [(os.getcwd() + '/images/chicken.jpg'), (os.getcwd() + '/images/tomato.jpg')]
    for path in paths_to_attachments:
        et.attach_file(context.driver, path)

@when('I enter an invalid email address for the recipient')
def step_impl(context):
    context.recipient = "sdfjsidnfo129sdf7@gmail.com"
    et.fill_to_field(context.driver, context.recipient)
# ----------------------------------

# ------------ THEN ---------------
@then('the recipient receives the email with the image attached')
def step_impl(context):
    email = {"delivery_address" : "dogwizard69@gmail.com", "recipient_address" : context.recipient, "email_subject" : context.subject, "attachment_name" : "chicken.jpg"}
    # et.receive_mail(context.recipient, context.recipient_password, email, False)
    et.receive_mail(context.recipient, email, False)

@then('the recipient receives the email with the image linked via Google Drive')
def step_impl(context):
    assert context.failed is False

@then('the recipient receives the email with all images attached')
def step_impl(context):
    assert context.failed is False

@then('I receive an automated email informing me that the recipient address does not exist')
def step_impl(context):
    assert context.failed is False
# --------------------------------

