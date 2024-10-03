import pywhatkit as kit
import time

contacts = {
    "Test": "+1234567890"
}

# Your message
message = "Hello! This is a test message."

def send_whatsapp_messages():
    """
    Sends a WhatsApp message to multiple contacts from the 'contacts' dictionary.

    For each contact, the message is scheduled to be sent 1 minute from the current time
    to allow WhatsApp Web to load.

    This function opens WhatsApp Web in your default browser, logs in using a QR code if not logged in, 
    and sends the specified message to each contact in the list.

    A small delay (`time.sleep(5)`) is introduced after each message is scheduled to avoid errors 
    due to rapid successive calls.

    Args:
        None: All required data is taken from the global 'contacts' and 'message' variables.

    Returns:
        None: The function only sends messages and prints confirmation to the console for each contact.
    """
    for name, number in contacts.items():
        kit.sendwhatmsg(number, message, time.localtime().tm_hour, time.localtime().tm_min + 1) # Sends the WhatsApp message and gives 1 minute to load
        time.sleep(5) # Waiting to ensure that messages are sent one by one
        print(f"Sent message to {name} - {number}")

send_whatsapp_messages()
