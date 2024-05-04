
from flask import Flask, render_template, request
import os
import time
from urllib import parse

app = Flask(__name__)

# Function to send ADB commands
def send_adb_command(command):
    os.system(f"adb shell input {command}")

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form['command']
    if "UrL" in command:
        command = command.replace('UrL','')
        command = parse.unquote(command)
        print(command)
        os.system(f"adb shell am start -a android.intent.action.VIEW -d {command}")
        time.sleep(3)
        return 'OK'
    if "ZhIbO" == command:
        os.system("adb shell am start -n com.tcl.tv/com.tcl.tv.TVActivity")
        time.sleep(3)
        return 'OK'
    if "YoUtUbE" == command:
        os.system("adb shell am start com.liskovsoft.smarttubetv.beta")
        time.sleep(3)
        return 'OK'
    if "ViDeO" == command:
        os.system("adb shell am start -n com.tcl.videocall/.MainActivity")
        time.sleep(3)
        os.system("adb shell input keyevent KEYCODE_DPAD_LEFT")
        os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")
        os.system("adb shell input keyevent KEYCODE_ENTER")
        return 'OK'
    send_adb_command(command)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host="::", port="8888")

