from sqlalchemy import text
from db_helper import db

def save_article(title, author, year):
    result=db.session.execute(
        text("""
        INSERT INTO items (type, title, author, year)
        VALUES ('article', :title, :author, :year)
        RETURNING id;
        """),
        {"title": title, "author": author, "year": year}
    )

    general_id=result.fetchone()[0]

    db.session.execute(
        text("""
        INSERT INTO articles (general_id)
        VALUES (:general_id);
        """),
        {"general_id": general_id}
    )

    db.session.commit()
