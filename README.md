Mouse Mover for macOS
A simple utility to keep your Mac active by automatically moving the mouse at set intervals. This is useful for preventing your computer from going to sleep or showing you as "away" in messaging apps like Slack or Microsoft Teams.

Demo
Features
Simple and intuitive user interface built with PyQt6.

Set a custom time interval in seconds for mouse movement.

Start and Stop the mouse movement on demand.

Can be packaged as a standalone .app for easy use.

Building and Running the App
This project uses Python and PyQt6. You can either run it directly from the source code or package it into a standalone .app file.

Prerequisites

Ensure you have Python 3 installed on your Mac. Then, install the required libraries using pip:

pip3 install PyQt6 pyautogui

Running from Source

To run the application directly from the script, navigate to the project directory and run:

python3 mouse_mover.py

Creating a Standalone macOS App with PyInstaller

To create a .app file that you can run like any other application, we will use PyInstaller.

1. Install PyInstaller:
If you don't already have it, install PyInstaller.

pip3 install pyinstaller

2. Prepare an Icon (Optional):
If you want a custom icon for your app, create a macOS icon file (e.g., MouseMover.icns) and place it in the same directory as the mouse_mover.py script.

3. Build the App:
Navigate to the project directory in your terminal and run the following command:

pyinstaller --name "MouseMover" --onefile --windowed --icon="MouseMover.icns" mouse_mover.py

--name "MouseMover": Sets the name of your final application.

--onefile: Packages everything into a single executable file.

--windowed: Crucial for macOS. This creates a proper .app bundle and prevents a terminal window from appearing when you run it.

--icon="MouseMover.icns": Attaches your custom icon to the app.

4. Find Your App:
PyInstaller will create a dist folder. Inside, you will find MouseMover.app. You can move this to your main /Applications folder for easy access.

Important: Granting Permissions on macOS
For the application to control your mouse, you must grant it Accessibility permissions. This is a standard security feature in macOS.

Open System Settings > Privacy & Security > Accessibility.

Click the + button.

Navigate to where you saved MouseMover.app and add it to the list.

Make sure the toggle next to MouseMover is turned on.

License
This project is licensed under the MIT License.

