import re

def protect_data(text):
    # This example scrubs obvious email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    scrubbed_text = re.sub(email_pattern, "[EMAIL_REDACTED]", text)
    
    # You can add more patterns for names, phone numbers, etc.
    return scrubbed_text

# Test your engine
raw_input = "My name is John Doe and my private email is john.doe@google.com"
protected_output = protect_data(raw_input)
# print(f"Original: {raw_input}")
# print(f"Protected: {protected_output}")