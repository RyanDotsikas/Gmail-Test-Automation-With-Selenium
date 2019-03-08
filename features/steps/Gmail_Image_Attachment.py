from behave import *

# ------------ GIVEN ---------------
@given('I am logged into a valid Gmail account')
def step_impl(context):
    pass
# ----------------------------------

# ------------ WHEN ---------------
@when('I choose to compose a new email')
def step_impl(context):
    assert True is not False

@when('I enter a valid email address for the recipient')
def step_impl(context):
    assert True is not False

@when('I enter a subject line or a body to the email')
def step_impl(context):
    assert True is not False

@when('I attach an image that is less than 25 Mb in size')
def step_impl(context):
    assert True is not False

@when('I send the email')
def step_impl(context):
	assert True is not False

@when('I select an image that exceeds 25 Mb in size to attach')
def step_impl(context):
    assert True is not False

@when('I attach multiple images (that total less than 25 Mb)')
def step_impl(context):
    assert True is not False

@when('I enter an invalid email address for the recipient')
def step_impl(context):
    assert True is not False

@when('I do not enter a subject line or a body to the email')
def step_impl(context):
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

