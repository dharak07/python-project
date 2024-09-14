from datetime import datetime, timedelta

# Get current date and time
now = datetime.now()
print(f"Current Date and Time: {now}")

# Create a specific date object
my_birthday = datetime(1990, 5, 15)
print(f"My Birthday: {my_birthday}")

# Date arithmetic: Adding 10 days to the current date
future_date = now + timedelta(days=10)
print(f"Date 10 days from now: {future_date}")

# Formatting datetime as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Parsing a string into a datetime object
date_string = "2024-01-01 12:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed Date: {parsed_date}")