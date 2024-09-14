import re

# 1. Searching for a pattern in a string using re.search()
pattern = r"\d{3}-\d{3}-\d{4}"  # A phone number pattern: 123-456-7890
text = "Call me at 123-456-8390 or 987-654-3210."

match = re.search(pattern, text)
if match:print(f"Found a match: {match.group()}")
else:print("No match found")

# 2. Finding all occurrences using re.findall()
all_matches = re.findall(pattern, text)
print(f"All phone numbers: {all_matches}")

# 3. Substituting text using re.sub()
replaced_text = re.sub(pattern, "XXX-XXX-XXXX", text)
print(f"After substitution: {replaced_text}")

# 4. Splitting a string using re.split()
sentence = "apple,banana;orange|grape"
split_result = re.split(r"[;|,]", sentence)
print(f"Split result: {split_result}")
# 5. Using re.match() to check the start of the string
text_start = "123-456-7890 is the number."
match_start = re.match(pattern, text_start)
if match_start:
    print(f"Match at start: {match_start.group()}")
else:
    print("No match at the start")
