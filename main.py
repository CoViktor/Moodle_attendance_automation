from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

# Setup
driver = webdriver.Edge()
url_attendance = 'https://moodle.becode.org/mod/attendance/view.php?id=90'


def get_credentials():
    if os.path.exists('./credentials.txt'):
        with open('./credentials.txt', 'r') as credentials:
            login= credentials.readline().strip()
            pw = credentials.readline().strip()
    else:
        login= input('No credentials found. Please give your login name to be written in the credentials file for future reference: ')
        pw = input('Please give your password to be written in the credentials file for future reference: ')
        with open('./credentials.txt', 'w') as credentials:
            credentials.write(login + '\n')
            credentials.write(pw)
    return login, pw


def login_handling():
    login, password = get_credentials()
    # Locating input fields
    login_input = driver.find_element("xpath", '//input[@id="username"]')
    password_input = driver.find_element("xpath", '//input[@id="password"]')
    # Clearing and filling input fields
    login_input.clear()
    login_input.send_keys(login)
    password_input.clear()
    password_input.send_keys(password)
    # Finalizing the login & waiting a second
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)


# Starting driver
driver.get(url_attendance)
# Check if 'login' is in the URL
if 'login' in driver.current_url:
    login_handling()

# Locate & click attendance button
# attendance_button = driver.find_element(By.XPATH, "")
# attendance_button.click()

# close the driver after use
driver.quit()

# ----------------------------- CLEANUP & UPGRAGE ---------------------------------------

# Put everything in utils & define functions to import here -> mind file pathing

# Clean code & generate docstrings

# Updates / Upgrades in readme:
# check if headless works too -> maybe javascript needs to load
# foreseen issues:id=90 of url could change
# check if works on different dates 