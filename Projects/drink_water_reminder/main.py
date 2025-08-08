import time  # For adding delay between notifications
from plyer import notification  # For sending desktop notifications

# Infinite loop to keep reminding
while True:
    print("Please sip some water!")  # Console message
    notification.notify(
        title="Please drink some water",  # Notification title
        message="You need to drink some water",  # Notification message
    )
    time.sleep(3)  # Wait for 3 seconds before next reminder
