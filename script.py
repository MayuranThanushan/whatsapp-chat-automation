import pywhatkit as kit
import time

contacts = {
    "Test": "+1234567890"
}

# Your message
message = "Hello! This is a test message."

def send_whatsapp_messages():
    for name, number in contacts.items():
        kit.sendwhatmsg(number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
        time.sleep(5)
        print(f"Sent message to {name} - {number}")

send_whatsapp_messages()
