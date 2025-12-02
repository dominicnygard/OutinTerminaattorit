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

bibtex_type_mapping = {
    "articles": "article",
    "books": "book",
    "inproceedings": "inproceedings",
    "booklets": "booklet",
}

def to_bibtex(reference: dict) -> str: 
    bib_type=bibtex_type_mapping.get(reference["type"], reference["type"])
    possible_fields = ["author", "title", "year", "journal", "volume", "number", "pages", "month", "notes", "publisher", "address", "booktitle", "editor", "series", "organization", "howpublished"]
    fields = {}
    for key in possible_fields: 
        value=reference.get(key)
        if value not in (None, ""):
            fields[key]=value
    
    #bibTex rivit
    bibtex_lines = [f"@{bib_type}{{{reference['id']},"]
    for k, v in fields.items():
        bibtex_lines.append(f"  {k} = {{{v}}},")

    if len(bibtex_lines) > 1:
        bibtex_lines[-1] = bibtex_lines[-1].rstrip(',')  # Poista viimeisen rivin pilkku
    
    bibtex_lines.append("}")

    return "\n".join(bibtex_lines)