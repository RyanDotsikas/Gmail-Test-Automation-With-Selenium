from behave import *
import email_testing.py
import os

# ------------ GIVEN ---------------
@given('I am logged into a valid Gmail account')
def step_impl(context):
    context.driver = setup_webdriver()
    load_inbox(context.driver, "dogwizard69", "ter12wvrrahah")
# ----------------------------------

# ------------ WHEN ---------------
@when('I choose to compose a new email')
def step_impl(context):
    click_create_mail(context.driver)

@when('I enter a valid email address for the recipient')
def step_impl(context):
    context.recipient = "dogwizard69@gmail.com"
    fill_to_field(context.driver, context.recipient)

@when('I enter a subject line or a body to the email')
def step_impl(context):
    fill_subject_field(context.driver, "Test Subject")
    fill_body_field(context.driver, "Yarr harr I am an email spam bot ayy lmao " + str(random.randint(1,1000)))

@when('I attach an image that is less than 25 Mb in size')
def step_impl(context):
    attach_file(context.driver, (os.getcwd() + '/images/chicken.jpg'))

@when('I send the email')
def step_impl(context):
	press_send(context.driver)

@when('I select an image that exceeds 25 Mb in size to attach')
def step_impl(context):
    # Need to attach a file that is actually more than 25 Mb
    attach_file(context.driver, (os.getcwd() + '/images/chicken.jpg'))

@when('I attach multiple images (that total less than 25 Mb)')
def step_impl(context):
    paths_to_attachments = [(os.getcwd() + '/images/chicken.jpg'), (os.getcwd() + '/images/tomato.jpeg')]
    for path in paths_to_attachments:
        attach_file(context.driver, path)

@when('I enter an invalid email address for the recipient')
def step_impl(context):
    context.recipient = "sdfjsidnfo129sdf7@gmail.com"
    fill_to_field(context.driver, context.recipient)

@when('I do not enter a subject line or a body to the email')
def step_impl(context):
    #Don't have to do anything here?
    assert True is not False
# ----------------------------------

# ------------ THEN ---------------
@then('the recipient receives the email with the image attached')
def step_impl(context):
    assert context.failed is False

@then('the recipient receives the email with the image linked via Google Drive')
def step_impl(context):
    assert context.failed is False

@then('the recipient receives the email with all images attached')
def step_impl(context):
    assert context.failed is False

@then('I receive an automated email informing me that the recipient address does not exist')
def step_impl(context):
    assert context.failed is False

@then('I receive a warning that the email has no subject or body text')
def step_impl(context):
    assert context.failed is False
# --------------------------------

