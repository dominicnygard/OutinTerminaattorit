from db_helper import db
from sqlalchemy import text

def save_article(title, author, year):
    result=db.session.execute(
        text("""
        INSERT INTO items (type)
        VALUES ('article')
        RETURNING id;
        """)
    )

    general_id=result.fetchone()[0]

    db.session.execute(
        text("""
        INSERT INTO articles (general_id, title, author, year)
        VALUES (:general_id, :title, :author, :year);
        """), 
        {"general_id": general_id, "title": title, "author": author, "year": year}
    )

    db.session.commit()
