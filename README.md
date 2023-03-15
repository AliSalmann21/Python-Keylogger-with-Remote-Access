# Keylogger

This is a Python keylogger that logs all keystrokes and sends the data to a remote server. It also has features such as taking screenshots, capturing webcam images, and stealing saved passwords. This tool is intended for educational purposes only and should not be used for any unethical activities.

## Features

* Logs all keystrokes
* Sends keystroke data to a remote server
* Takes screenshots at set intervals
* Captures images from webcam
* Steals saved passwords from web browsers
* Has a hidden mode option
* Can be set to run automatically on startup

## Dependencies

* Python 3
* pynput
* Pillow
* OpenCV
* PyInstaller (for building executables)

## Installation

1. Clone the repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Edit the server IP address and port in the `config.py` file.
4. Run the `main.py` file to start the keylogger.

## Usage

The keylogger will start running as soon as you run the `main.py` file. It will log all keystrokes and send the data to the specified server. Screenshots will be taken at regular intervals and saved to the `screenshots` folder. Webcam images will be saved to the `webcam` folder. Saved passwords will be saved to the `passwords.txt` file.

To exit the keylogger, press the `ESC` key. To run the keylogger in hidden mode, pass the `-h` argument when running the `main.py` file.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
