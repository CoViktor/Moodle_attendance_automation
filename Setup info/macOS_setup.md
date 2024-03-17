# macOS Setup
Runs on Safari, since this is installed by default on every Mac computer.

### Local Setup
- Step 1: Clone the repo locally.
- Step 2: Install the required dependencies (see requirements.txt).
    - Open Terminal and run ```pip3 install -r requirements.txt```
- Step 3: Setup the holidays and campus_days lists at the top of `main_apple.py`.
- Step 4: Run `main_apple.py` once to input and store your credentials.
    - The file `credentials.txt` is added to `.gitignore` and won't be pushed to GitHub.

### Automator & Calendar for Scheduling
We will use Automator to create an application that runs our script, and Calendar to schedule it.

- Step 1: Enable 'Allow Remote Automation' in Safari.
    - In Safari, go to Safari > Preferences > Advanced and check "Show Develop menu in menu bar".
    - In the Develop menu, select "Allow Remote Automation".
- Step 2: Creating an Application with Automator
    - Open Automator (found in your Applications folder).
    - Choose to create a new "Application".
    - Search for "Run Shell Script" in the Actions search bar on the left, then drag it to the workflow on the right.
    - In the text area for the script, input the following command, making sure to replace <path_to_your_script> with the actual path to your Python script:
    ```/usr/bin/python3 <path_to_your_script>/main_apple.py```
    - Save the application to your desired location, e.g., MoodleAttendance.app.
- Step 3: Scheduling with Calendar
    - Open Calendar.
    - Create a new event for the time you want your script to run.
    - Double-click on the event to edit it, then click on 'Add Alert', 'Custom...', then 'Open file'.
    - Select 'Other...' and navigate to where you saved your Automator application (e.g., MoodleAttendance.app).
 - Set the alert to 'At the time of event'.
 - Repeat for any other times you need the script to run.

### Permissions and Security Settings
- Depending on your macOS version, you may need to grant specific permissions for Automator or Terminal to control your computer. This is a crucial step to ensure the Automator application can run the script successfully.
- Go to System Preferences > Security & Privacy > Privacy tab. Scroll down to 'Accessibility' and click the lock icon to make changes. You might need to add Terminal or Automator to the list of applications allowed to control your computer.

This setup uses native macOS applications and requires no additional downloads beyond the required Python packages. Make sure to test the setup by running the Automator application directly and checking if the script operates as expected.

### Issues
- Contact me if you run into issues, so that we can troubleshoot together.
- If you were able to solve the issue yourself, and the solution could be added to this setup file, please notify me so the information can be updated.

Find me on [LinkedIn](https://www.linkedin.com/in/viktor-cosaert/).