from db_helper import db
from sqlalchemy import text

from config import references

def save_references(input, type):
    result=db.session.execute(
        text("""
        INSERT INTO items (type, title, year, author)
        VALUES (:type, :title, :year, :author)
        RETURNING id;
        """),
        {"type": type, **input}
    )

    del input['title']
    del input['year']
    del input['author']

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
    result = db.session.execute(text("SELECT id, type, title, author, year FROM items"))

    references.set_references(result)
    return references.get_all()

def search_references(query):
    results = []
    all_references = references.get_all() if references.get_all() else get_citations()
    for ref in all_references:
        if query.lower() in ref["title"].lower():
            results.append(ref)
    return results

def get_references_by_id(id):
    item = db.session.execute(
        text("SELECT * FROM items WHERE id = :id"),
        {"id": id}
    ).fetchone()

    if not item: 
        return None
    
    reference={
        "id": item.id,
        "type": item.type,
        "title": item.title,
        "year": item.year,
        "author": item.author
    }

    specific = db.session.execute(
        text(f"SELECT * FROM {item.type} WHERE general_id = :id"),
        {"id": id}
    ).fetchone()

    if specific: 
        for k in specific._mapping.keys():
            reference[k] = dict(specific._mapping)[k]
    
    return reference

