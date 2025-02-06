README.md

# LoVeBiTe - Ransomware-like System Lock Screen 💻🔒  

LoVeBiTe is a Python-based program that simulates a device lock screen, displaying a ransom-like message and requiring the correct password to unlock the device. If the user fails to input the correct password within a given number of attempts, a simulated Blue Screen of Death (BSOD) appears. 🚫💻  

This project was created for **educational purposes** to demonstrate the usage of GUI elements with `tkinter` and basic programming concepts like password checking, attempts limitation, and system alerts.  

## Features 🌟  

- Customizable password protection 🔑  
- Interactive GUI lock screen built with `tkinter` 🖥️  
- Lock screen with a ransom message and instructions for "unlocking" the device 💰  
- Virtual numeric keypad for user password entry ⌨️  
- Option to simulate a BSOD if too many incorrect password attempts are made 💥  
- Configurable number of login attempts 🎯  
- Easy-to-use interface 💡  

## Prerequisites 📦  

Before running the script, make sure you have:  

- **Python 3** 🐍  
- **`tkinter`** (usually bundled with Python) 📚  
- **`keyboard`** ⌨️ (`pip install keyboard`)  
- **`pyinstaller`** (optional, for making an `.exe` file) ⚙️  

## Installation ⚙️  

Clone the repository:  
```bash
git clone https://github.com/N3tw0rk-h4x0r/LoVeBiTe.git

Navigate to the project folder:

cd LoVeBiTe

Install the required dependencies:

pip install -r requirements.txt

Run the Python script:

python3 lovebite.py

Optional: Convert to .exe file

If you need a standalone Windows executable:

pip install pyinstaller  # Install PyInstaller if you haven't already

pyinstaller --onefile --noconsole --clean --icon=icon.ico lovebite.py

If the first command does not work, try:

python -m pyinstaller --onefile --noconsole --clean --icon=icon.ico lovebite.py

The executable will be created in the dist/ directory inside the project folder.
Usage 💻

Once the program is executed, it will display the lock screen. You will need to input the correct password to unlock the device. If the wrong password is entered three times, the program will simulate a BSOD. 💥

    After entering the correct password, a success message will appear ✅.
    If incorrect password attempts reach zero, a BSOD simulation will be triggered 💻💥.

How It Works 🛠️

    The lock screen is displayed with a ransom-like message and instructions for "unlocking." 💸
    The user is required to input a password. 🔐
    If the correct password is entered, the screen will unlock and the program will exit. 🚪✅
    If incorrect passwords are entered, the number of attempts decreases. ⏳
    After 3 failed attempts, the program will trigger a simulated BSOD. 💻⚠️

Customization ✨

    You can change the password variable in the code to set your own password. 🔑
    Modify the ransom message in the lock_text and steps variables. 📝
    Customize the number of attempts allowed by changing the count variable. 🎯

License 📜

This project is licensed under the MIT License - see the LICENSE file for details. ⚖️
⚠️ Disclaimer

This project is for educational purposes only. It is meant to demonstrate GUI locking mechanisms using tkinter and password validation in Python.

🚨 Do not use this for malicious activities! Unauthorized use of this script on devices without the owner's consent may be illegal. The author is not responsible for any misuse of this code.
