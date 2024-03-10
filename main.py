from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

url_attendance = 'https://moodle.becode.org/mod/attendance/view.php?id=90'
url_login = "https://moodle.becode.org/login/index.php"

driver.get(url_attendance)

# Gaat eerst naar login 
# -> name & pass not saved -> steek in aparte file & zet die in gitignore


# Zoek buttons om te klikken


driver.close()


