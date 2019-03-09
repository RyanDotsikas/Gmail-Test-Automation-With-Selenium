Feature: Gmail Image Attachment

Scenario: Sending an email with a small .jpg image attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
And I attach a .jpg format image that is less than 25 Mb in size
And I send the email
Then the recipient receives the email with the image attached

Scenario: Sending an email with a small .png image attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
And I attach a .png format image that is less than 25 Mb in size
And I send the email
Then the recipient receives the email with the image attached

Scenario: Sending an email with a large .jpg image attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
But I attach a .jpg format image that exceeds 25 Mb in size
And I send the email
Then the recipient receives the email with the image linked via Google Drive

Scenario: Sending an email with multiple .jpg images attached
Given I am logged into a valid Gmail account
When I choose to compose a new email
And I enter a valid email address for the recipient
And I enter a subject line or a body to the email
And I attach multiple .jpg format images (that total less than 25 Mb)
And I send the email
Then the recipient receives the email with all images attached

Scenario: Sending an email to an invalid address
Given I am logged into a valid Gmail account
When I choose to compose a new email
But I enter an invalid email address for the recipient
And I enter a subject line or a body to the email
And I attach a .jpg format image that is less than 25 Mb in size
And I send the email
Then I receive an automated email informing me that the recipient address does not exist