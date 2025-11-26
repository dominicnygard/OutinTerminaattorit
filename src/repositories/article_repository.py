from db_helper import db

def save_article(title, author, year):
    result=db.session.execute(
        """
        INSERT INTO items (content, done)
        VALUES (:content, FALSE)
        RETURNING id;
        """, 
       {"content": f"Article: {title}"}
    )

    general_id=result.fetchone()[0]

    db.session.execute(
        """
        INSERT INTO articles (general_id, title, author, year)
        VALUES (:general_id, :title, :author, :year);
        """, 
        {"general_id": general_id, "title": title, "author": author, "year": year}
    )

    db.session.commit()
