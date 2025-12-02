class UserInputError(Exception):
    pass

def validate_todo(content):
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
          raise UserInputError("Todo content length must be smaller than 100")

reference_fields = {
    "articles": {"required": ["title", "author", "year", "journal"], "optional": ["volume", "number", "pages", "month", "notes"]},
    "books": {"required": ["title", "author", "year", "publisher", "address"], "optional": []},
    "inproceedings": {"required": ["title", "author", "year", "booktitle"], "optional": ["editor", "volume", "number", "series", "pages", "address", "month", "organization", "publisher"]},
    "booklets": {"required": ["title", "author", "year", "howpublished", "address"], "optional": ["editor", "volume", "number", "series", "organization", "month", "note"]},
    "conferences": {"required": ["title", "author", "year", "booktitle"], "optional": ["editor", "volume", "number", "series", "pages", "address", "month", "organization", "publisher", "note"]},
    "inbooks": {"required": ["title", "author", "year", "booktitle", "publisher"], "optional": ["editor", "volume", "number", "series", "address", "edition", "month", "pages", "note"]},
    "incollections": {"required": ["title", "author", "year", "booktitle", "publisher"], "optional": ["editor", "volume", "number", "series", "pages", "address", "month"]},
    "inproceedings": {"required": ["title", "author", "year", "booktitle"], "optional": ["editor", "volume", "number", "series", "pages", "address", "month", "organization", "publisher"]},
    "manuals": {"required": ["title", "year"], "optional": ["author", "organization", "address", "edition", "month", "note"]},
    "mastertheseses": {"required": ["title", "year", "author", "school"], "optional": ["type", "address", "month", "note"]},
    "phdtheseses": {"required": ["title", "year", "author", "school"], "optional": ["type", "address", "month", "note"]},
    "proceedings": {"required": ["title", "year"], "optional": ["editor", "volume", "number", "series", "address", "month", "publisher"]},
    "techreports": {"required": ["title", "year", "author", "institution", "number"], "optional": []},
    "unpublisheds": {"required": ["title", "year", "author", "institution", "number"], "optional": []}
    
}