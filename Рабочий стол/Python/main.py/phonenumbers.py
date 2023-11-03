def is_phone(phone: str):
    codes = ['8', '+7']
    for code in codes:
        code_len = len(code)
    if phone.startswith(code):
        valid_length = len