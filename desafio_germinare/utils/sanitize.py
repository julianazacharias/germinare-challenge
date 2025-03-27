def sanitize(string):
    sanitized_string = string.upper()
    sanitized_string = ' '.join(sanitized_string.split())

    return sanitized_string
