from random import choice
from re import sub

class UserInputError(Exception):
    pass

def validate_field(content):
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
        raise UserInputError("Todo content length must be smaller than 100")

reference_fields = {
    "articles": {
        "required": 
            ["title", "author", "year", "journal"],
        "optional":
            ["volume", "number", "pages", "month", "notes"]},
    "books": {
        "required":
            ["title", "author", "year", "publisher", "address"],
        "optional":
            []},
    "booklets": {
        "required":
            ["title", "author", "year", "howpublished", "address"],
        "optional":
            ["editor", "volume", "number", "series",
             "organization", "month", "note"]},
    "conferences": {
        "required":
            ["title", "author", "year", "booktitle"],
        "optional":
            ["editor", "volume", "number", "series", "pages",
             "address", "month", "organization", "publisher", "note"]},
    "inbooks": {
        "required":
            ["title", "author", "year", "booktitle", "publisher"],
        "optional":
            ["editor", "volume", "number", "series", "address",
             "edition", "month", "pages", "note"]},
    "incollections": {
        "required":
            ["title", "author", "year", "booktitle", "publisher"],
        "optional":
            ["editor", "volume", "number", "series",
             "pages", "address", "month"]},
    "inproceedings": {
        "required":
            ["title", "author", "year", "booktitle"],
        "optional":
            ["editor", "volume", "number", "series", "pages",
              "address", "month", "organization", "publisher"]},
    "manuals": {
        "required":
            ["title", "year"],
        "optional":
            ["author", "organization", "address",
             "edition", "month", "note"]},
    "mastertheseses": {
        "required":
            ["title", "year", "author", "school"],
        "optional":
            ["type", "address", "month", "note"]},
    "phdtheseses": {
        "required":
            ["title", "year", "author", "school"],
        "optional":
            ["type", "address", "month", "note"]},
    "proceedings": {
        "required":
            ["title", "year"],
        "optional":
            ["editor", "volume", "number", "series",
             "address", "month", "publisher"]},
    "techreports": {
        "required":
            ["title", "year", "author", "institution", "number"],
        "optional":
            []},
    "unpublisheds": {
        "required":
            ["title", "year", "author", "institution", "number"],
        "optional":
            []}
}

bibtex_type_mapping = {
    "articles": "article",
    "books": "book",
    "inproceedings": "inproceedings",
    "booklets": "booklet",
}

def to_bibtex(reference):
    bib_type=bibtex_type_mapping.get(reference["type"], reference["type"])
    possible_fields = ["author", "title", "year", "journal", "volume",
                       "number", "pages", "month", "notes", "publisher",
                       "address", "booktitle", "editor", "series", "organization",
                       "howpublished"]
    fields = {}
    for key in possible_fields:
        value=reference.get(key)
        if value not in (None, ""):
            fields[key]=value

    bibtex_lines = [f"@{bib_type}{{{citation_key(reference['title'],
                                                 reference['author'],
                                                 reference['year'])},"]
    for k, v in fields.items():
        bibtex_lines.append(f"  {k} = {{{v}}},")

    if len(bibtex_lines) > 1:
        bibtex_lines[-1] = bibtex_lines[-1].rstrip(',')

    bibtex_lines.append("}")

    return "\n".join(bibtex_lines)

def citation_key(title, author, year):
    excluded_words = {"the", "an", "a", "of", "and", "for", "with", "on", "in", "to", "at"}
    cleaned_title = sub(r"[^A-Za-z0-9\s]", "", title)
    last_name = author.split()[-1].capitalize()
    key_word = choice(
        [w.capitalize() for w in cleaned_title.lower().split() if not w in excluded_words]
    )
    return last_name + year + key_word
