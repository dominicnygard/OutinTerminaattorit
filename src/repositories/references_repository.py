from db_helper import db
from sqlalchemy import text

from config import references

def save_references(input, type):
    result=db.session.execute(
        text("""
        INSERT INTO items (type)
        VALUES (:type)
        RETURNING id;
        """),
        {"type": type}
    )

    general_id=result.fetchone()[0]
    temp = {'general_id': general_id}
    input['general_id'] = general_id
    references = dict(temp, **input)

    sql_columns = ', '.join(references.keys())
    sql_values = ", :".join(references.keys())
    sql_values = ':' + sql_values

    db.session.execute(
        text(f"""
        INSERT INTO {type} ({sql_columns})
        VALUES ({sql_values});
        """), 
        references
    )

    db.session.commit()

def get_citations():
    result = db.session.execute(text("SELECT id, type FROM items"))

    references.set_references(result)
    return references.get_all()