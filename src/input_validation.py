

def validate_year(year):
    if not year.isdigit():
        return "Year must consist of digits"
    if not len(year) == 4:
        return "Year must be in format (YYYY)"
    if int(year) < 1900 or int(year) > 2099:
        return "Year out of range"

def validate_title(title):
    pass

def validate_author(author):
    pass


