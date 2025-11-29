class UserInputError(Exception):
    pass

def validate_todo(content):
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
          raise UserInputError("Todo content length must be smaller than 100")

reference_fields = {
    "articles": ["title", "author", "year", "journal", "volume", "number", "pages", "month", "notes"],
    "books": ["title", "author", "year", "publisher", "address"],
    "inproceedings": ["title", "author", "year", "booktitle", "editor", "volume", "number", "series", "pages", "address", "month", "organization", "publisher"],
    "booklets": ["title", "author", "year", "howpublished", "address", "editor", "volume", "number", "series", "organization", "month", "note"],
    
}