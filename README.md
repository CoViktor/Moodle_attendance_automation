# Automated Moodle Attendance Logger 🤖
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 🏢 Description

As part of the AI trainee program at BeCode.org, attendance is mandatory and tracked twice each day. To challenge myself and learn more about Selenium, I've automated my attendance logging. This script runs at the required times each day with Windows Task Scheduler, using Selenium for web interaction, and includes a feature to skip holidays. 

<img src="https://cdn.schoolstickers.com/products/en/819/A159592-00.png" width="400" height="auto"/>

## 📦 Repo structure
```
.
├── .gitignore
├── credentials.txt (created on first run)
├── main.py
├── README.md
└── requirements.txt
```

## 🚧 Installation 

1. Clone the repository to your local machine.

    ```
    git clone https://github.com/CoViktor/Moodle_attendance_automation.git
    ```

2. Navigate to the project directory and install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## ✔️ Usage 

This script automates the process of logging attendance on the BeCode platform. It checks the current date against a list of predefined holidays and logs in to mark attendance if it's not a holiday.

Ensure credentials.txt is set up by running the script once. If the file doesn't exist, the script will prompt you to enter your credentials, which will be saved for future use.

Schedule the script to run at the required logging times using Task Scheduler or a similar tool.

Here's a snippet from main.py demonstrating the core functionality:

```python
def get_credentials():

def login_handling():

driver.get(url_attendance)
if 'login' in driver.current_url:
    login_handling()
attendance_button = driver.find_element(By.XPATH, "_")
attendance_button.click()

driver.quit()
```
## ⏱️ Timeline
This project took an afternoon to complete.

## 🔧 Updates & Upgrades
### Recent Updates
- **11/03/24**: Added pathing to the disappearing attendance button.
- **12/03/24**: 1| Upgraded pathing to the attendance button to ignore 'check out' button. 2| Added feature that thecks weekday and selects location to check in from ('On campus' or 'At home') accordingly.

### Planned Upgrades
- **Date-time dependency**: Due to the nature of Moodle, updates might change buttons. Updates will account for changes when necessary.
- **Location dependency**: Script needs to be updated to adjust the location to campus or home, depending on the day.

## 📌 Personal Situation
This project was undertaken as a learning challenge during my AI Bootcamp at [BeCode.org](https://becode.org/). It has been a valuable experience in automating real-world tasks and learning to use Selenium for web automation, as well as Windows Task Scheduler for further automation purposes.

Connect with me on [LinkedIn](https://www.linkedin.com/in/viktor-cosaert/).
