class UserInputError(Exception):
    pass

def validate_todo(content):
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
          raise UserInputError("Todo content length must be smaller than 100")

reference_fields = {
    "article": ["title", "author", "year"],
    "book": ["title", "author", "year"],
    "inproceeding": ["title", "author", "year"]
}