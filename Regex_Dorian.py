import re 

text = """
URL: https://www.example.com, https://subdomain.example.org/page
Email_Address : user@example.com, firstname.lastname@company.co.uk
Phone_numbers : (123) 456-7890, 123-456-7890, 123.456.7890
Currency_amounts : $19.99, $1,234.56
"""

patterns = {
    "URL": r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^\s]*)?",
    "Email_Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Phone_number": r"(\(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})",
    "Currency_amounts": r"\$\d{1,3}(,\d{3})*(\.\d{2})?|\$\d+(\.\d{2})?"
}

for key in patterns:
    matches = re.findall(patterns[key], text)
    # If matches contain tuples (from grouped regex), flatten them
    if matches and isinstance(matches[0], tuple):
        matches = [''.join(match) for match in matches]
    print(f"{key}:")
    for m in matches:
        print(f"  ➤ {m}")
