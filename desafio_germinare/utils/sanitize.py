def sanitize(string):
    sanitized_string = string.strip().upper()
    sanitized_string = ' '.join(sanitized_string.split())
    return sanitized_string
