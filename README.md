# Mouse Mover for macOS
A simple utility to keep your Mac active by automatically moving the mouse at set intervals. This is useful for preventing your computer from going to sleep or showing you as "away" in messaging apps like Slack or Microsoft Teams.


## Demo

https://youtu.be/lmnxJm7RP5Y?si=GVXU3rJaDJkLKX6D

## Prerequisites

Ensure you have Python 3 installed on your Mac. Then, install the required libraries using pip:

```bash
pip3 install PyQt6 pyautogui
```

## Running from Source

To run the application directly from the script, navigate to the project directory and run:

```
python3 mouse_mover.py
```

## Creating a Standalone macOS App with PyInstaller
To create a `.app` file that you can run like any other application, we will use PyInstaller.

If you don't already have it, install PyInstaller.
```
pip3 install pyinstaller
```

Navigate to the project directory in your terminal and run the following command:

```
pyinstaller --name "MouseMover" --onefile --windowed --icon="MouseMover.icns" mouse_mover.py
```

PyInstaller will create a `dist` folder. Inside, you will find `MouseMover.app`. You can move this to your main `/Applications` folder for easy access.

## Important: Granting Permissions on macOS

For the application to control your mouse, you must grant it Accessibility permissions. This is a standard security feature in macOS.

1. Open System Settings > Privacy & Security > Accessibility.
2. Click the + button.
3. Navigate to where you saved MouseMover.app and add it to the list.
4. Make sure the toggle next to MouseMover is turned on.

## License
This project is licensed under the MIT License.
