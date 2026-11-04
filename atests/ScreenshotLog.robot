*** Settings ***
Documentation       Screenshot images belong in log.html.
...                 Consoles and log listeners must not receive the screenshot message.

Library             util/screenshotlog.py


*** Test Cases ***
Screenshot Is In The Log And Not On The Console
    [Documentation]    Base64 and file screenshots are embedded for log.html
    ...    and are hidden from log listeners such as the RobotCode debug console.
    Reset Log Listener
    Log    listener sees ordinary messages
    Publish Base64 Screenshot    CONSOLE-HIDDEN-BASE64-TOKEN
    Publish File Screenshot    console-hidden-screenshot.png
    Log Should Contain Screenshot    data:image/png;base64,CONSOLE-HIDDEN-BASE64-TOKEN
    Log Should Contain Screenshot    console-hidden-screenshot.png
    Log Listener Should Have Received    listener sees ordinary messages
    Log Listener Should Not Have Received    CONSOLE-HIDDEN-BASE64-TOKEN
    Log Listener Should Not Have Received    console-hidden-screenshot.png
