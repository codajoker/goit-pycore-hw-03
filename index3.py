import re

def normalize_phone(phone_number: str) -> str:
    cleaned_number = re.sub(r"[^\d+]", "", phone_number).strip()
    
    if cleaned_number.startswith("380"):
        return f"+{cleaned_number}"
    
    if not cleaned_number.startswith("+"):
        return f"+38{cleaned_number}"
    
    return cleaned_number


