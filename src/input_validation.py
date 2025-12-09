
def validate_type(type):
    pass

def validate_title(title):
    if not (2 <= len(title) <= 250):
        return "Title length must be in range 2-250"

def validate_year(year):
    if not year.isdigit():
        return "Year must consist of digits"
    if not len(year) == 4:
        return "Year must be in format (YYYY)"
    if int(year) < 1900 or int(year) > 2099:
        return "Year out of range"

def validate_author(author):
    if not (2 <= len(author) <= 150):
        return "Author length must be in range 2-150"
    # check if only letters
    if not author.isalpha():
        return "Author must consist of only letters"
    
def validate_journal(journal):
    pass

def validate_publisher(publisher):
    pass

def validate_address(address):
    pass



# add more

# contain into validate_text_input etc

# goes into validate text: title
# booktitle, journal, publisher, 

#validate numbers: pages, 



