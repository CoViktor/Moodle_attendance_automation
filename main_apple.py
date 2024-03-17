from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
from datetime import datetime

# ::::::::::::::::::SETUP::::::::::::::::::::
# Add your holidays here, so that the script doesn't run when it doesn't have to
holidays = ['2024-03-22', '2024-04-01', '2024-04-02', '2024-04-03',
            '2024-04-04', '2024-04-05', '2024-05-01', '2024-04-09',
            '2024-07-05', '2024-07-08', '2024-07-09', '2024-07-10', 
            '2024-07-11', '2024-07-12', '2024-08-15']
today = datetime.now().strftime('%Y-%m-%d')
# Clarify the days you usually attend from campus here, as opposed to the days at home
# (0 = monday, 1 = tuesday, 2 = wednesday, ...)
campus_days = [0, 3]
# ::::::::::::::::::END SETUP::::::::::::::::::::
if today in holidays:
    exit()

# Using Safari WebDriver; make sure to enable 'Allow Remote Automation' in Safari's Develop menu
driver = webdriver.Safari()
url_attendance = 'https://moodle.becode.org/mod/attendance/view.php?id=90'


def get_credentials():
    '''Retrieves login credentials from a local 'credentials.txt' file.
    
    If the 'credentials.txt' file does not exist, prompts the user to enter their login name and password,
    which are then saved to 'credentials.txt' for future use.
    
    Returns:
        tuple: A tuple containing the login name and password.
    '''
    credentials_path = os.path.join(os.path.expanduser('~'), 'credentials.txt')  
    if os.path.exists(credentials_path):
        with open(credentials_path, 'r') as credentials:
            login = credentials.readline().strip()
            pw = credentials.readline().strip()
    else:
        login = input('No credentials found. Please give your login name to be written in the credentials file for future reference: ')
        pw = input('Please give your password to be written in the credentials file for future reference: ')
        with open(credentials_path, 'w') as credentials:
            credentials.write(login + '\n')
            credentials.write(pw)
    return login, pw


def login_handling():
    '''   
    Handles the login process for a web page using Selenium.
    '''
    login, password = get_credentials()
    # Locating input fields
    login_input = driver.find_element(By.XPATH, '//input[@id="username"]')
    password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
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
attendance_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Check in')]")
attendance_button.click()
time.sleep(5)

# Picking the location based on day of the week
today_weekday = datetime.now().weekday()
if today_weekday in campus_days:
    location = "oncampus"
else:
    location = "athome"

select_element = driver.find_element(By.ID, "id_location")
location_select = Select(select_element)
if location == "oncampus":
    location_select.select_by_value("oncampus")
else:
    location_select.select_by_value("athome")
time.sleep(1)    

# Locate & click save changes button
save_button = driver.find_element(By.XPATH, "//input[@id='id_submitbutton']")
save_button.click()
time.sleep(3)

# close the driver after use
driver.quit()