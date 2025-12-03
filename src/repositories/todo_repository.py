from sqlalchemy import text
from config import db

from config import references

def get_citations():
    result = db.session.execute(text("SELECT id, type, title, author, year FROM items"))

    references.set_references(result)
    return references.get_all()

def set_done(todo_id):
    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
    db.session.execute(sql, { "id": todo_id })
    db.session.commit()

def create_todo(content):
    sql = text("INSERT INTO todos (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()
