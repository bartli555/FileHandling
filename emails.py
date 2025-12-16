import re

def nadawca_emaila(email_content):
    sender_pattern = r"From:.*<([^>]+)>"
    match = re.search(sender_pattern, email_content)
    if match:
        return match.group(1)
    return None

def odbiorca_emaila(email_content):
    recipient_pattern = r"To:.*<([^>]+)>"
    match = re.search(recipient_pattern, email_content)
    
    if match:
        return match.group(1)
    return None

def email_subject(email_content):
    subject_pattern = r"Subject: (.*)"
    match = re.search(subject_pattern, email_content)
    
    if match:
        return match.group(1)
    return None

def email_body(email_content):
    parts = email_content.split('\n\n', 1)
    
    if len(parts) > 1:
        return parts[1].strip()
    return None