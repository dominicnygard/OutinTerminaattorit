import re

months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
types = [
    "articles",
    "books",
    "booklets",
    "conferences",
    "inbooks",
    "incollections",
    "inproceedings",
    "manuals",
    "mastertheseses",
    "phdtheseses",
    "proceedings",
    "techreports",
    "unpublished",
]

def validate_title(title):
    if not 2 <= len(title) <= 250:
        return "Title length must be in range 2-250"

def validate_year(year):
    if not year.isdigit():
        return "Year must consist of digits"
    if not len(year) == 4:
        return "Year must be in format (YYYY)"
    if int(year) < 1900 or int(year) > 2099:
        return "Year out of range"

def validate_author(author):
    if not 2 <= len(author) <= 150:
        return "Author length must be in range 2-150"
    if not author.replace(" ", "").isalpha():
        return "Author input must consist of only letters"
    
def validate_text(text, max_len=200):
    if len(text) == 1:
        return f"Field with input {text} must be at least 2 characters"
    if not (len(text) <= max_len):
        return "Input length too long. Max input length is 200 characters"
    
def validate_month(month):
    if month.lower() not in months:
        return "Month must be in format 'jan', 'feb'..."

def validate_pages(pages):
    pattern = r'^\d+(--\d+)?(,\s*\d+(--\d+)?)*$'
    if not re.match(pattern, pages):
        return "Pages must be a number or range (e.g., 12 or 12--19,25--30)"

def validate_integer(integer):
    if not str(integer).isdigit():
        return f"Field with input {integer} must contain only numbers"


VALIDATION_METHODS = {
    "author":       validate_author,
    "editor":       validate_text,
    "title":        validate_title,
    "journal":      validate_text,
    "publisher":    validate_text,
    "organization": validate_text,
    "school":       validate_text,
    "institution":  validate_text,
    "address":      validate_text,
    "booktitle":    validate_text,
    "note":         validate_text,
    "howpublished": validate_text,
    "edition":      validate_text,

    "year":         validate_year,
    "month":        validate_month,
    "pages":        validate_pages,
    "volume":       validate_integer,
    "number":       validate_integer,

}
