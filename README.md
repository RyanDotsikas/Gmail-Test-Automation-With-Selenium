# ECSE428_A2

This project was created for Assignment 2 of ECSE428, with the goal of automating the testing of Gmail by sending emails with image files attached. The project tests 5 different scenarios that vary the type of recipient and image file. It is written in Python, utilizing Selenium Web Driver and Cucumber's Python version: Behave to conduct all tests.

Installation Instructions:
1. Download and Install Python 3
  a. You can check your current python version by typing ‘python’ into the command line
    i.If you have python version 2.x installed, you can still install python 3 and use either by typing python for 2.x and python3 for 3.x
  b. Official Download: https://www.python.org/downloads/ 
  c. If you have two python versions installed: replace pip with pip3 in the following commands
2. Install Selenium
  a. Type ‘pip install selenium’ into the command line (read next line)
3. Install Webdriver_manager_module
  a. You may be informed that you require the Webdriver_manager module
  b. If so, type ‘pip install webdriver-manager’ in the command line
  c. You may then have to repeat Step 2 to trigger the installation again
4. Install Behave, the Python version of Cucumber
  a. Type ‘pip install behave’

Operation Instructions:
1. Open the command line
2. Navigate to the project folder: ECSE428_A2
3. Enter the following in the command line to run the tests: ‘behave’
4. When the Gmail web page is loaded, log in to a Gmail account of your choice
  a. This is to avoid Gmail’s security measures, such as Captcha or Two-Step Authentication, that are designed to stop bots such as this
