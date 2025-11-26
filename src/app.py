from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_citations, create_todo, set_done
from config import app, test_env
from util import validate_todo
from repositories.article_repository import save_article

@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", citations=citations) 

@app.route("/new_todo")
def new():
    return render_template("new_todo.html")

@app.route("/create_todo", methods=["POST"])
def todo_creation():
    content = request.form.get("content")

    try:
        validate_todo(content)
        create_todo(content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_todo")

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

@app.route("/articles/new")
def new_article():
    return render_template("new_article.html")

@app.route("/articles/create", methods=["POST"])
def create_article():
    title=request.form["title"]
    author=request.form["author"]
    year=request.form["year"]

    save_article(title, author, year)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
