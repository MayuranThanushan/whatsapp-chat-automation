
# WhatsApp Chat Automation

This project provides a Python script to automate sending WhatsApp messages to multiple contacts using the `pywhatkit` library. The script allows you to schedule and send messages to contacts at a specified time via WhatsApp Web.

## Features
- **Send WhatsApp Messages to Multiple Contacts**: Automatically send a message to multiple contacts provided in a list.
- **WhatsApp Web Automation**: The script uses WhatsApp Web to send messages and requires login using QR code (if not already logged in).
- **Message Scheduling**: Messages are scheduled to be sent 1 minute from the current time to ensure WhatsApp Web has enough time to load.

## Requirements

- Python 3
- The following Python libraries:
  - `pywhatkit`: For sending messages via WhatsApp Web
  - `time`: For managing the scheduling and delays between messages

### Install Dependencies

To install the required Python packages, run the following command:

```bash
pip install pywhatkit
```

## Important Notes

- **Login to WhatsApp Web**: The script uses WhatsApp Web, so ensure you are logged in. If not, it will prompt you to scan the QR code.
- **Delays**: The script includes a small delay (`time.sleep()`) between sending messages to avoid issues with sending too quickly.
- **Message Timing**: The message is scheduled to be sent 1 minute from the current time. Adjustments can be made by modifying the time calculation in the script.

## Limitations
- This script is not intended for bulk messaging or spamming. Be mindful of WhatsApp's rules and limitations.
- The script relies on WhatsApp Web, so it is subject to the availability and reliability of the web interface.
- You need to keep your browser open and stay logged into WhatsApp Web for the script to function properly.
