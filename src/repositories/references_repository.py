from sqlalchemy import text
from db_helper import db

from config import references

def save_references(ref_input, ref_type):
    result=db.session.execute(
        text("""
        INSERT INTO items (type, title, year, author)
        VALUES (:type, :title, :year, :author)
        RETURNING id;
        """),
        {"type": ref_type, **ref_input}
    )

    del ref_input['title']
    del ref_input['year']
    del ref_input['author']

    general_id=result.fetchone()[0]
    temp = {'general_id': general_id}
    ref_input['general_id'] = general_id
    save_ref = dict(temp, **ref_input)

    sql_columns = ', '.join(save_ref.keys())
    sql_values = ", :".join(save_ref.keys())
    sql_values = ':' + sql_values

    db.session.execute(
        text(f"""
        INSERT INTO {ref_type} ({sql_columns})
        VALUES ({sql_values});
        """),
        save_ref
    )

    db.session.commit()

def get_citations():
    result = db.session.execute(text("SELECT id, type, title, author, year FROM items"))

    references.set_references(result)
    return references.get_all()

def search_references(query=None, year=None, author=None):
    results = []
    all_references = references.get_all() if references.get_all() else get_citations()
    for ref in all_references:
        if query:
            if not query.lower() in ref.get("title", "").lower():
                continue
        if year:
            if not year in ref.get("year", ""):
                continue
        if author:
            if not author.lower() in ref.get("author", "").lower():
                continue
        results.append(ref)
    return results

def filter_references(refs, types):
    results = []
    types = [t.lower() for t in types]
    for ref in refs:
        if ref.get("type", "").lower() in types:
            results.append(ref)
    return results

def get_references_by_id(ref_id):
    item = db.session.execute(
        text("SELECT * FROM items WHERE id = :id"),
        {"id": ref_id}
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
        {"id": ref_id}
    ).fetchone()

    if specific:
        for k in specific._mapping.keys():
            reference[k] = dict(specific._mapping)[k]

    return reference
