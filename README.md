# KeyLogger
Python Keylogger (Educational Purpose Only)
This is a simple keylogger implemented in Python using the pynput library. It captures keyboard input and logs it to a file (keylog.txt). The logger records normal key presses, as well as special keys like Enter, Tab, Backspace, and Space.

⚠️ Disclaimer:
This project is intended for educational purposes only. Do not use it to monitor or log keystrokes on devices you do not own or have explicit permission to monitor. Unauthorized keylogging is illegal and unethical. 

$ Features $
Records all key presses, including special keys.
Logs data in real-time to keylog.txt.
Periodically saves the log every 10 seconds using threading.
Stops logging when ESC is pressed.

📦 Requirements
Python 3.x
pynput

Install dependencies:
pip install pynput

Run the script:
python keylogger.py
The program will begin listening for key presses and log them to keylog.txt. Press ESC to stop the keylogger.

📁 Output
Logs are saved to a file named keylog.txt in the same directory. The output format includes timestamps and keys pressed.

