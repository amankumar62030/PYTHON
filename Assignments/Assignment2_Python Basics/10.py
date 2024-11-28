#  Write a python script to display the current date and time. First create variables to
#  store date and time, then display date and time in proper format (like: 13-8-2022 and
#  9:00 PM

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Create variables for date and time
date = current_datetime.strftime("%d-%m-%Y")  # Format: DD-MM-YYYY
time = current_datetime.strftime("%I:%M %p")  # Format: HH:MM AM/PM

# Display date and time
print("Date:", date)
print("Time:", time)
