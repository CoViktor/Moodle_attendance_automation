# Windows setup
Runs on edge, since this is installed by default on each Windows computer.

### Local setup
- Step 1: Clone the repo locally.
- Step 2: Install the required dependencies (see requirements.txt).
    - ``` pip install requirements.txt ```
- Step 3: Setup the holidays and campus_days lists at the top of main.py
- Step 4: Run main.py once to input and store your credentials.
    - The file credentials.txt is added to .gitignore and won't be pushed to github.

### Task Scheduler setup
- Step 1: Download the Edge Driver
    - Download link: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH
    - Version available at Settings-help in the browser.
    - Install in a folder you can remember, since we'll need the filepath below.
- Step 2: Navigate to Task Scheduler (search it in start menu).
- Step 3: Create a new task (Action > Create Task).
    - General tab:
        - Fill in Name (and description)
        - Optional: check 'Run only when usir is logged on' and 'Run with highest privileges'
        - Configure for: pick your Windows version
    - Triggers tab:
        - New trigger:
        - Begin the task: on a schedule
        - Settings: One time, start (today), 9am
        - Recur every 1 weeks on: Monday to Friday
        - New trigger:
        - Same settings, but 13.30pm
    - Actions tab:
        - New...
        - Action: Start a program
        - Programs/script: "C:\path\to\your\python\driver\Python311\python.exe" (quotation marks might be needed) -> find this by entering ```where python``` in your terminal.
        - Add arguments: "C:\path\to\main.py" (quotation marks might be needed)
        - Start in: C:\path\to\project\folder\Moodle_attendance_automation 
        (NO QUOTATION MARKS!)
    - Conditions tab:
        - Optional: toggle off the Power settings
    - OK
- Step 4: Right click Run your new task to test if it works.

