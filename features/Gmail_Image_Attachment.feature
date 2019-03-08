Feature: Gmail Image Attachment

Scenario: Sending an email with a small image attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
And I attach an image that is less than 25 Mb in size
And I send the email
Then the recipient receives the email with the image attached

Scenario: Sending an email with a large image attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
But I select an image that exceeds 25 Mb in size to attach
And I send the email
Then the recipient receives the email with the image linked via Google Drive

Scenario: Sending an email with multiple images attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
And I attach multiple images (that total less than 25 Mb)
And I send the email
Then the recipient receives the email with all images attached

Scenario: Sending an email to an invalid address
Given I am logged into a valid Gmail account
When I choose to compose a new email
But I enter an invalid email address for the recipient
And I enter a subject line or a body to the email
And I attach an image that is less than 25 Mb in size
And I send the email
Then I receive an automated email informing me that the recipient address does not exist

Scenario: Sending an email without a subject or body text
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
But I do not enter a subject line or a body to the email
And I attach an image that is less than 25 Mb in size
And I send the email
Then I receive a warning that the email has no subject or body text


